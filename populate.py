import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viewSeq.settings')

import django

django.setup()

from traceSeq.models import Seq,  Comment


def populate():
    # lizard_ hexon
    h1 = """MEPQREFFHIAGRSAKEYLSENLVQFIQATQNYFNIGEKFRDPYVAPSAGVTTDRSQKLQ
LRVVPIQTEDNVNYYKARFTLNVGDNRLVDLGSSYFDIKGTLDRGPSFKPYGGTAYNPLA
PKSAPINSAFTVGNDTHFVAQLPQTYAAGGTGVTEAIQQQVSGVDPNPQVGQPNYAGPVV
VNTTNNAGLGRIVSADSEGQQFPCYGAYAPPQSAGGDVSTAAVTKTYINTTNNNGRVSGT
MATDTITWENPDAHFADFVDDRRATAAGNRPNYIGFRDNFIGMMYYNSGSNTGSFSSQTQ
QLNIVLDLNDRNSELSYQYLLADLTSRWHYFALWNQAVDDYDHHVRILENDGYEEGPPNL
AFPPHVISNPFAPAAVGTGMTVNEQQQTAAVTANTVALIGYGNIPAVEMNLPANLKRTFL
YSNVAMYLPDTYKFTPANVDLPENHLSYGYINGRLPLPNIVDTWTDIGARWSLDVMDTVN
PFNHHRNTGLKYRSQLLGNGRYCDFHIQVPQKFFAIKNLLLLPGTYNYEWYFRKDPNMVL
QSTLGNDLRADGASITYTQINLYVSFFPMNYDTQSELELMLRNATNDQNFSDYLGAVNNL
YQIPAGSSTVVVNIPDRSWGAFRGWSFTRLKVSETPRIGATQDPNFQYSGSIPYLDGTFY
LSHTFQRCSIQWDSSVPWPGNDRMLTPNWFEIKRPINQDAEGNDTMQSNLTKDFFMVQMA
ASYNQGYQGFNWPNCTKHYGFINNFEPMSRQVPEYGANYPNLMAAYLANPQTMPIWNNCG
FQQKTATNVLLERCGHPYVANWPYPLSGRNAVPNQVTERKFLVDRYLWQIPFSSNFLNMG
TLTDLGQNVMYANSSHSLNMQFTVDPMTEPTYLMLLFGVFDQVVINQPTRSGISVAYLRL
PFASGSAAT"""
    ex = '''MELAALCRWGLLLALLPPGAASTQVCTGTDMKLRLPASPETHLDMLRHLYQ
GCQVVQGNLELTYLPTNASLSFLQDIQEVQGYVLIAHNQVRQVPLQRLRIVRGTQLF
EDNYALAVLDNGDPLNNTTPVTGASPGGLRELQLRSLTEILKGGVLIQRNPQLCYQD
TILWKDIFHKNNQLA'''
    s = add_seq(h1, 'h1-adenovirus-lizard')
    #   add_seq(ex,'test')
    add_struct('helix', 3, 8, s)
    add_struct('helix', 15, 18, s)
    add_struct('helix', 21, 29, s)
    add_struct('helix', 37, 39, s)
    add_struct('helix', 91, 93, s)
    add_struct('helix', 278, 280, s)
    add_struct('helix', 289, 291, s)
    add_struct('helix', 313, 324, s)
    add_struct('helix', 332, 334, s)
    add_struct('helix', 343, 346, s)
    add_struct('helix', 411, 427, s)
    add_struct('helix', 430, 432, s)
    add_struct('helix', 448, 453, s)
    add_struct('helix', 458, 461, s)
    add_struct('helix', 474, 477, s)
    add_struct('helix', 488, 497, s)
    add_struct('helix', 536, 539, s)
    add_struct('helix', 571, 581, s)
    add_struct('helix', 584, 586, s)
    add_struct('helix', 632, 634, s)
    add_struct('helix', 653, 656, s)
    add_struct('helix', 662, 664, s)
    add_struct('helix', 701, 703, s)
    add_struct('helix', 712, 723, s)
    add_struct('helix', 742, 744, s)
    add_struct('helix', 845, 847, s)
    add_struct('helix', 849, 853, s)

    add_struct('beta_strand', 60, 63, s)
    add_struct('beta_strand', 67, 70, s)
    add_struct('beta_strand', 74, 83, s)
    add_struct('beta_strand', 94, 103, s)
    add_struct('beta_strand', 128, 130, s)
    add_struct('beta_strand', 137, 139, s)
    add_struct('beta_strand', 188, 193, s)
    add_struct('beta_strand', 224, 228, s)
    add_struct('beta_strand', 239, 244, s)
    add_struct('beta_strand', 253, 257, s)
    add_struct('beta_strand', 265, 268, s)
    add_struct('beta_strand', 274, 276, s)
    add_struct('beta_strand', 294, 297, s)
    add_struct('beta_strand', 376, 378, s)
    add_struct('beta_strand', 386, 388, s)
    add_struct('beta_strand', 502, 510, s)
    add_struct('beta_strand', 524, 533, s)
    add_struct('beta_strand', 540, 542, s)
    add_struct('beta_strand', 554, 565, s)
    add_struct('beta_strand', 588, 591, s)
    add_struct('beta_strand', 596, 603, s)
    add_struct('beta_strand', 609, 614, s)
    add_struct('beta_strand', 624, 631, s)
    add_struct('beta_strand', 665, 672, s)
    add_struct('beta_strand', 676, 678, s)
    add_struct('beta_strand', 745, 752, s)
    add_struct('beta_strand', 816, 823, s)
    add_struct('beta_strand', 828, 831, s)
    add_struct('beta_strand', 858, 864, s)
    add_struct('beta_strand', 871, 878, s)
    add_struct('beta_strand', 880, 886, s)
    add_struct('beta_strand', 894, 900, s)


def add_struct(type, init, finish, s):
    init -= 1
    finish -= 1
    if type == "beta_strand":
        type = 'b'
    elif type == "helix":
        type = 'h'
    elif type == "loop":
        type = 'l'
    else:
        type = '.'
    struct = s.struct
    struct = struct[0:init] + type * (finish - init + 1) + struct[finish:]
    s.struct = struct
    s.save()


def add_seq(seq, seqName):
    # remove newlines
    seq = seq.replace('\n', '')
    seq = seq.replace('\r', '')
    state  = "." * len(seq)
    struct = "." * len(seq)
    s = Seq.objects.get_or_create(seq=seq, state=state, struct=struct, seqName=seqName)[0]
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()