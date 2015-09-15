from django.http import HttpResponse
from django.shortcuts import render
from models import Seq
from django.shortcuts import render_to_response
from django.template import RequestContext
from itertools import cycle


def index(request):
    #using GET get sequece and state
    #http://127.0.0.1:8000/traceSeq/?seqId=2
    aa_init = -1
    aa_end  = -1
    aa = None
    doWhat = None
    if 'aaStruct' in request.GET:
        seqId = request.session['seqId']
        aa = request.GET['aaStruct']
        doWhat='struct'
    elif 'aaState' in request.GET:
        seqId = request.session['seqId']
        aa = request.GET['aaState']
        doWhat='state'
    else:
        seqId = request.GET['seqId']
        request.session['seqId'] = seqId
        doWhat = None
        #just in case
        if 'aa_init' in request.session:
             del request.session['aa_init']

    s   = Seq.objects.filter(id=int(seqId))[0]
    if doWhat is not None:
      if 'aa_init' in request.session:
        if doWhat == 'state':
            keys=['x','!','.']
            list = s.state
        elif doWhat == 'struct':
            keys=['h','b','l','.']
            list = s.struct
        aa_init = request.session['aa_init']
        aa_end = int(aa) + 1
        print("aa_init end",aa_init,aa_end)
        for aaI in range (aa_init,aa_end+1):
            result = list[0:aaI-1]+keys[(keys.index(list[aaI-1])+1)%len(keys)]+list[aaI:]
            list = result
        if doWhat == 'state':
            s.state = result
        elif doWhat == 'struct':
            s.struct = result
        s.save()
        del request.session['aa_init']
        aa_init = -1
        aa_end  = -1
      else:
          request.session['aa_init'] = int(aa) + 1
          aa_init = int(aa)
    #create dictionary
    context_dict={}
    #context_dict = {'seq': s.seq}
    #context_dict['state']=s.state
    #context_dict['struct']=s.struct
    seq_struct_state = zip(s.seq, s.struct,s.state)
    context_dict['seq_struct_state']=seq_struct_state
    context_dict['seqName']=s.seqName
    context_dict['aa_init']=aa_init
    context_dict['aa_end']=aa_end

    return render_to_response('traceSeq/index.html',
                                  context_dict,
                                  context_instance=RequestContext(request))

#def updateState(request):
#    #http://127.0.0.1:8000/traceSeq/updateState/?seqId=2&aa=34
#    #http://127.0.0.1:8000/traceSeq/updateState/?aa=34
#    #seqId = request.GET['seqId']
#    aa    = int(request.GET['aa'])
#    seqId = request.session['seqId']
#    print("seqId aa", seqId, aa)
#    s   = Seq.objects.filter(id=int(seqId))[0]
#    st = s.state
#    stInt = [int(x) for x in st.split(',')]
#    print("stInt", stInt)
#    stInt[aa] = (stInt[aa] + 1)
#    print("stIntC", stInt)
#    s.state =  ','.join(map(str,stInt))
#    print("state", s.state)
#    s.save()
#    #call the template.
#    context_dict={}
#    #create dictionary
#    context_dict = {'seq': s.seq}
#    context_dict['state']=s.state.replace(',','')
#    context_dict['seqName']=s.seqName
#    st   = Struct.objects.filter(seq=s)
#    context_dict['structures']=st
#    return render(request, 'traceSeq/index.html', context_dict)
