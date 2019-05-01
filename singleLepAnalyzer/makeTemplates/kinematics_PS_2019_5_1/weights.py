#!/usr/bin/python

targetlumi = 41298. # 1/pb

genHTweight={}
genHTweight['WJetsMG100'] = 0.998056#https://github.com/jmhogan/GenHTweight/blob/master/WJetsToLNuSFs.txt
genHTweight['WJetsMG200'] = 0.978569
genHTweight['WJetsMG400'] = 0.928054
genHTweight['WJetsMG600'] = 0.856705
genHTweight['WJetsMG800'] = 0.757463
genHTweight['WJetsMG1200']= 0.608292
genHTweight['WJetsMG2500']= 0.454246

genHTweight['DYMG100'] = 1.007516#https://github.com/jmhogan/GenHTweight/blob/master/DYJetsToLLSFs.txt
genHTweight['DYMG200'] = 0.992853
genHTweight['DYMG400'] = 0.974071
genHTweight['DYMG600'] = 0.948367
genHTweight['DYMG800'] = 0.883340
genHTweight['DYMG1200']= 0.749894
genHTweight['DYMG2500']= 0.617254

BR={}
BR['BW'] = 0.5
BR['TZ'] = 0.25
BR['TH'] = 0.25
BR['TTBWBW'] = BR['BW']*BR['BW']
BR['TTTHBW'] = 2*BR['TH']*BR['BW']
BR['TTTZBW'] = 2*BR['TZ']*BR['BW']
BR['TTTZTZ'] = BR['TZ']*BR['TZ']
BR['TTTZTH'] = 2*BR['TZ']*BR['TH']
BR['TTTHTH'] = BR['TH']*BR['TH']

BR['TW'] = 0.5
BR['BZ'] = 0.25
BR['BH'] = 0.25
BR['BBTWTW'] = BR['TW']*BR['TW']
BR['BBBHTW'] = 2*BR['BH']*BR['TW']
BR['BBBZTW'] = 2*BR['BZ']*BR['TW']
BR['BBBZBZ'] = BR['BZ']*BR['BZ']
BR['BBBZBH'] = 2*BR['BZ']*BR['BH']
BR['BBBHBH'] = BR['BH']*BR['BH']

# Number of processed MC events (before selections)
nRun={}
nRun['TTJets'] = 14188545. #need negative counts
nRun['TTJetsPH'] = 111068128.#
nRun['TTJetsHad0'] = 129211104*0.8832 # from integral 130262340.0, file TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_hadd.root
nRun['TTJetsHad700'] = 129211104*0.0921 + 38520877*0.457
nRun['TTJetsHad1000'] = 129211104*0.02474 + 21302221*0.457
nRun['TTJetsSemiLep0'] = 109194238*0.8832 # from integral 110085096.0, file TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_hadd.root
nRun['TTJetsSemiLep700'] = 109194238*0.0921 + 38520877*0.438
nRun['TTJetsSemiLep1000'] = 109194238*0.02474 + 21302221*0.438
nRun['TTJets2L2nu0'] = 68595608*0.8832 # from integral 69155808.0, file TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_hadd.root
nRun['TTJets2L2nu700'] = 68595608*0.0921 + 38520877*0.105
nRun['TTJets2L2nu1000'] = 68595608*0.02474 + 21302221*0.105
nRun['TTJetsPH700mtt'] = 38520877. + 129211104*0.0921 + 109194238*0.0921 + 68595608*0.0921 #from 39258853, file TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TTJetsPH1000mtt'] = 21302221. + 129211104*0.02474 + 109194238*0.02474 + 68595608*0.02474 # from integral 22458751.0, file TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg
nRun['Ts'] = 6895750. # from integral 6898000.0, file ST_s-channel_top_leptonDecays_13TeV-PSweights_powheg-pythia_hadd.root
nRun['Tbs'] = 2952214. # from integral 2953000.0, file ST_s-channel_antitop_leptonDecays_13TeV-PSweights_powheg-pythia_hadd.root
nRun['Tt'] = 122688200. # from integral 122688200.0, file ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root
nRun['Tbt']= 64818800. # from integral 64818800.0, file ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root
nRun['TtW'] = 7601399. # from integral 7660001.0, file ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root
nRun['TbtW'] = 7686032. # from integral 7745276.0, file ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root
nRun['WJets'] = 6776900. # from 9908534.
nRun['WJetsMG'] = 86731806. 
nRun['WJetsMG100'] = 79356685.
nRun['WJetsMG200'] = 21192211. # from integral 21250517.0, file WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG400'] = 14250114. # from integral 14313274.0, file WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG600'] = 21582309. # from integral 21709087.0, file WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG800'] = 20272990. # from integral 20432728.0, file WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG1200']= 19991892. # from integral 20258624.0, file WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG2500']= 20629585. # from integral 21495421.0, file WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsPt100'] = 120124110.*(1.-2.*0.32) #Full =120124110, neg frac 0.32
nRun['WJetsPt250'] = 12022587.*(1.-2.*0.31555) #Full = 12022587, neg frac 0.31555 
nRun['WJetsPt400'] = 1939947.*(1.-2.*0.30952) #Full = 1939947, neg frac 0.30952
nRun['WJetsPt600'] = 1974619.*(1.-2.*0.29876) #Full = 1974619, neg frac 0.29876
nRun['DY'] = 123584520. # from 182359896, this is the ext1 sample
nRun['DYMG'] = 49082157. # from integral 49125561.0, file DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG100'] = 10607207.
nRun['DYMG200'] = 9653731.
nRun['DYMG400'] = 10008776.
nRun['DYMG600'] = 8292957.
nRun['DYMG800'] = 2668730.
nRun['DYMG1200']= 596079.
nRun['DYMG2500']=  399492.
nRun['WW'] = 7791498. # from integral 7791498.0, file WW_TuneCP5_13TeV-pythia8_hadd.root
nRun['WZ'] = 3928630. # from integral 3928630.0, file WZ_TuneCP5_13TeV-pythia8_hadd.root
nRun['ZZ'] = 1949768. # from integral 1949768.0, file ZZ_TuneCP5_13TeV-pythia8_hadd.root
nRun['QCDht100'] = 80684349.
nRun['QCDht200'] = 59351583. # from integral 59418819.0, file QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht300'] = 60205669. # from integral 60316577.0, file QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht500'] = 56032638. # from integral 56199340.0, file QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht700'] = 47518924. # from integral 47724800.0, file QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht1000'] = 16770762. # from integral 16882838.0, file QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht1500'] = 11508604. # from integral 11634434.0, file QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht2000'] = 5825566. # from integral 5941306.0, file QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['TTW'] = 9384328. # from integral 9425384.0, file ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_hadd.root
nRun['TTZ'] = 8519074. # from integral 8536618.0, file ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8_hadd.root
nRun['TTH'] = 9580578. # from integral 9783674.0, file ttH_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TTWl'] = 2692366. #from 4919674
nRun['TTWq'] = 430310. #from 833298
nRun['TTZl'] = 131210. #from 250000
nRun['TTZq'] = 351164. #from 749400
nRun['Hptb180'] = 404688. #Ngen=1499270
nRun['Hptb200'] = 400501. #Ngen=1473805
nRun['Hptb220'] = 402569. #Ngen=1499361 
nRun['Hptb250'] = 395891. #Ngen=1491475
nRun['Hptb300'] = 390646. #Ngen=1497522
nRun['Hptb350'] = 390221. #Ngen=1496373
nRun['Hptb400'] = 387746. #Ngen=1496088
nRun['Hptb450'] = 379926. #Ngen=1488753 CHECK NEG COUNT in MORIOND17!!!!! Sample not available yet
nRun['Hptb500'] = 400004. #Ngen=1500000
nRun['Hptb750'] = 377320. #Ngen=1488753 CHECK NEG COUNT in MORIOND17!!!!! Sample not available yet
nRun['Hptb800'] = 376326. #Ngen=1494646
nRun['Hptb1000'] = 376708. #Ngen=1491600
nRun['Hptb2000'] = 373174. #Ngen=1500000
nRun['Hptb3000'] = 377717. #Ngen=1497017

nRun['TTM1000BWBW'] = 842000.0*0.333*0.333
nRun['TTM1100BWBW'] = 745000.0*0.333*0.333#
nRun['TTM1200BWBW'] = 829000.0*0.333*0.333#
nRun['TTM1300BWBW'] = 847000.0*0.333*0.333#
nRun['TTM1400BWBW'] = 811000.0*0.333*0.333#
nRun['TTM1500BWBW'] = 827000.0*0.333*0.333#
nRun['TTM1600BWBW'] = 850000.0*0.333*0.333#
nRun['TTM1700BWBW'] = 836000.0*0.333*0.333#
nRun['TTM1800BWBW'] = 827000.0*0.333*0.333#
nRun['TTM1000THBW'] = 842000*0.333*0.333*2
nRun['TTM1100THBW'] = 745000.0*0.333*0.333*2#
nRun['TTM1200THBW'] = 829000.0*0.333*0.333*2#
nRun['TTM1300THBW'] = 847000.0*0.333*0.333*2#
nRun['TTM1400THBW'] = 811000.0*0.333*0.333*2#
nRun['TTM1500THBW'] = 827000.0*0.333*0.333*2#
nRun['TTM1600THBW'] = 850000.0*0.333*0.333*2#
nRun['TTM1700THBW'] = 836000.0*0.333*0.333*2#
nRun['TTM1800THBW'] = 827000.0*0.333*0.333*2#
nRun['TTM1000TZBW'] = 842000*0.333*0.333*2
nRun['TTM1100TZBW'] = 745000.0*0.333*0.333*2#
nRun['TTM1200TZBW'] = 829000.0*0.333*0.333*2#
nRun['TTM1300TZBW'] = 847000.0*0.333*0.333*2#
nRun['TTM1400TZBW'] = 811000.0*0.333*0.333*2#
nRun['TTM1500TZBW'] = 827000.0*0.333*0.333*2#
nRun['TTM1600TZBW'] = 850000.0*0.333*0.333*2#
nRun['TTM1700TZBW'] = 836000.0*0.333*0.333*2#
nRun['TTM1800TZBW'] = 827000.0*0.333*0.333*2#
nRun['TTM1000TZTZ'] = 842000*0.333*0.333
nRun['TTM1100TZTZ'] = 745000.0*0.333*0.333#
nRun['TTM1200TZTZ'] = 829000.0*0.333*0.333#
nRun['TTM1300TZTZ'] = 847000.0*0.333*0.333#
nRun['TTM1400TZTZ'] = 811000.0*0.333*0.333#
nRun['TTM1500TZTZ'] = 827000.0*0.333*0.333#
nRun['TTM1600TZTZ'] = 850000.0*0.333*0.333#
nRun['TTM1700TZTZ'] = 836000.0*0.333*0.333#
nRun['TTM1800TZTZ'] = 827000.0*0.333*0.333#
nRun['TTM1000TZTH'] = 842000*0.333*0.333*2
nRun['TTM1100TZTH'] = 745000.0*0.333*0.333*2#
nRun['TTM1200TZTH'] = 829000.0*0.333*0.333*2#
nRun['TTM1300TZTH'] = 847000.0*0.333*0.333*2#
nRun['TTM1400TZTH'] = 811000.0*0.333*0.333*2#
nRun['TTM1500TZTH'] = 827000.0*0.333*0.333*2#
nRun['TTM1600TZTH'] = 850000.0*0.333*0.333*2#
nRun['TTM1700TZTH'] = 836000.0*0.333*0.333*2#
nRun['TTM1800TZTH'] = 827000.0*0.333*0.333*2#
nRun['TTM1000THTH'] = 842000*0.333*0.333
nRun['TTM1100THTH'] = 745000.0*0.333*0.333#
nRun['TTM1200THTH'] = 829000.0*0.333*0.333#
nRun['TTM1300THTH'] = 847000.0*0.333*0.333#
nRun['TTM1400THTH'] = 811000.0*0.333*0.333#
nRun['TTM1500THTH'] = 827000.0*0.333*0.333#
nRun['TTM1600THTH'] = 850000.0*0.333*0.333#
nRun['TTM1700THTH'] = 836000.0*0.333*0.333#
nRun['TTM1800THTH'] = 827000.0*0.333*0.333#

nRun['BBM700TWTW'] = 814800.0*0.333*0.333
nRun['BBM800TWTW'] = 817200.0*0.333*0.333
nRun['BBM900TWTW'] = 799800.0*0.333*0.333
nRun['BBM1000TWTW'] = 850000.0*0.333*0.333
nRun['BBM1100TWTW'] = 806000.0*0.333*0.333
nRun['BBM1200TWTW'] = 850000.0*0.333*0.333
nRun['BBM1300TWTW'] = 758000.0*0.333*0.333
nRun['BBM1400TWTW'] = 728000.0*0.333*0.333
nRun['BBM1500TWTW'] = 675000.0*0.333*0.333
nRun['BBM1600TWTW'] = 769000.0*0.333*0.333
nRun['BBM1700TWTW'] = 832600.0*0.333*0.333
nRun['BBM1800TWTW'] = 850000.0*0.333*0.333
nRun['BBM700BHTW'] = 814800.0*0.333*0.333*2
nRun['BBM800BHTW'] = 817200.0*0.333*0.333*2
nRun['BBM900BHTW'] = 799800.0*0.333*0.333*2
nRun['BBM1000BHTW'] = 850000.0*0.333*0.333*2
nRun['BBM1100BHTW'] = 806000.0*0.333*0.333*2
nRun['BBM1200BHTW'] = 850000.0*0.333*0.333*2
nRun['BBM1300BHTW'] = 758000.0*0.333*0.333*2
nRun['BBM1400BHTW'] = 728000.0*0.333*0.333*2
nRun['BBM1500BHTW'] = 675000.0*0.333*0.333*2
nRun['BBM1600BHTW'] = 769000.0*0.333*0.333*2
nRun['BBM1700BHTW'] = 832600.0*0.333*0.333*2
nRun['BBM1800BHTW'] = 850000.0*0.333*0.333*2
nRun['BBM700BZTW'] = 814800.0*0.333*0.333*2
nRun['BBM800BZTW'] = 817200.0*0.333*0.333*2
nRun['BBM900BZTW'] = 799800.0*0.333*0.333*2
nRun['BBM1000BZTW'] = 850000.0*0.333*0.333*2
nRun['BBM1100BZTW'] = 806000.0*0.333*0.333*2
nRun['BBM1200BZTW'] = 850000.0*0.333*0.333*2
nRun['BBM1300BZTW'] = 758000.0*0.333*0.333*2
nRun['BBM1400BZTW'] = 728000.0*0.333*0.333*2
nRun['BBM1500BZTW'] = 675000.0*0.333*0.333*2
nRun['BBM1600BZTW'] = 769000.0*0.333*0.333*2
nRun['BBM1700BZTW'] = 832600.0*0.333*0.333*2
nRun['BBM1800BZTW'] = 850000.0*0.333*0.333*2
nRun['BBM700BZBZ'] = 814800.0*0.333*0.333
nRun['BBM800BZBZ'] = 817200.0*0.333*0.333
nRun['BBM900BZBZ'] = 799800.0*0.333*0.333
nRun['BBM1000BZBZ'] = 850000.0*0.333*0.333
nRun['BBM1100BZBZ'] = 806000.0*0.333*0.333
nRun['BBM1200BZBZ'] = 850000.0*0.333*0.333
nRun['BBM1300BZBZ'] = 758000.0*0.333*0.333
nRun['BBM1400BZBZ'] = 728000.0*0.333*0.333
nRun['BBM1500BZBZ'] = 675000.0*0.333*0.333
nRun['BBM1600BZBZ'] = 769000.0*0.333*0.333
nRun['BBM1700BZBZ'] = 832600.0*0.333*0.333
nRun['BBM1800BZBZ'] = 850000.0*0.333*0.333
nRun['BBM700BZBH'] = 814800.0*0.333*0.333*2
nRun['BBM800BZBH'] = 817200.0*0.333*0.333*2
nRun['BBM900BZBH'] = 799800.0*0.333*0.333*2
nRun['BBM1000BZBH'] = 850000.0*0.333*0.333*2
nRun['BBM1100BZBH'] = 806000.0*0.333*0.333*2
nRun['BBM1200BZBH'] = 850000.0*0.333*0.333*2
nRun['BBM1300BZBH'] = 758000.0*0.333*0.333*2
nRun['BBM1400BZBH'] = 728000.0*0.333*0.333*2
nRun['BBM1500BZBH'] = 675000.0*0.333*0.333*2
nRun['BBM1600BZBH'] = 769000.0*0.333*0.333*2
nRun['BBM1700BZBH'] = 832600.0*0.333*0.333*2
nRun['BBM1800BZBH'] = 850000.0*0.333*0.333*2
nRun['BBM700BHBH'] = 814800.0*0.333*0.333
nRun['BBM800BHBH'] = 817200.0*0.333*0.333
nRun['BBM900BHBH'] = 799800.0*0.333*0.333
nRun['BBM1000BHBH'] = 850000.0*0.333*0.333
nRun['BBM1100BHBH'] = 806000.0*0.333*0.333
nRun['BBM1200BHBH'] = 850000.0*0.333*0.333
nRun['BBM1300BHBH'] = 758000.0*0.333*0.333
nRun['BBM1400BHBH'] = 728000.0*0.333*0.333
nRun['BBM1500BHBH'] = 675000.0*0.333*0.333
nRun['BBM1600BHBH'] = 769000.0*0.333*0.333
nRun['BBM1700BHBH'] = 832600.0*0.333*0.333
nRun['BBM1800BHBH'] = 850000.0*0.333*0.333

nRun['X53X53M700left']  = 300000.
nRun['X53X53M700right'] = 299800.
nRun['X53X53M800left']  = 300000.
nRun['X53X53M800right'] = 300000.
nRun['X53X53M900left']  = 300000.
nRun['X53X53M900right'] = 300000.
nRun['X53X53M1000left']  = 300000.
nRun['X53X53M1000right'] = 300000.
nRun['X53X53M1100left']  = 300000.
nRun['X53X53M1100right'] = 300000.
nRun['X53X53M1200left']  = 300000.
nRun['X53X53M1200right'] = 299800.
nRun['X53X53M1300left']  = 299800.
nRun['X53X53M1300right'] = 300000.
nRun['X53X53M1400left']  = 300000.
nRun['X53X53M1400right'] = 299800.
nRun['X53X53M1500left']  = 296400.
nRun['X53X53M1500right'] = 300000.
nRun['X53X53M1600left']  = 300000.
nRun['X53X53M1600right'] = 300000.

#energy scale samples (Q^2)
nRun['TTJetsPHQ2U'] = 9933327.
nRun['TTJetsPHQ2D'] = 9942427.
nRun['TtWQ2U'] = 497600. #not used
nRun['TtWQ2D'] = 499200. #not used
nRun['TbtWQ2U'] = 500000. #not used
nRun['TbtWQ2D'] = 497600. #not used

#4 tops
nRun['4TM690'] = 849964.0


# Cross sections for MC samples (in pb)
xsec={}
xsec['DY'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG100'] = 147.4*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG200'] = 40.99*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG400'] = 5.678*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG600'] = 1.367*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG800'] = 0.6304*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG1200'] = 0.1514*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG2500'] = 0.003565*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJets'] = 831.76
xsec['WJets'] = 61526.7
xsec['WJetsMG'] = 61526.7
xsec['TTJetsPH'] = 831.76 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
#xsec['TTJetsPH0to700inc'] = 831.76
#xsec['TTJetsPH700to1000inc'] = 831.76*0.0921 #(xsec*filtering coeff.)
#xsec['TTJetsPH1000toINFinc'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['TTJetsHad0'] = 831.76*0.8832*0.457  ## BRs from PDG Top Review 2018: 45.7%/43.8%/10.5% 0/1/2 leptons
xsec['TTJetsHad700'] = 831.76*0.0921*0.457
xsec['TTJetsHad1000'] = 831.76*0.02474*0.457
xsec['TTJetsSemiLep0'] = 831.76*0.8832*0.438
xsec['TTJetsSemiLep700'] = 831.76*0.0921*0.438
xsec['TTJetsSemiLep1000'] = 831.76*0.02474*0.438
xsec['TTJets2L2nu0'] = 831.76*0.8832*0.105
xsec['TTJets2L2nu700'] = 831.76*0.0921*0.105
xsec['TTJets2L2nu1000'] = 831.76*0.02474*0.105
xsec['TTJetsPH700mtt'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000mtt'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['WJetsMG100'] = 1345.*1.21 # (1.21 = k-factor )# https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG200'] = 359.7*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG400'] = 48.91*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG600'] = 12.05*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG800'] = 5.501*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG1200'] = 1.329*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG2500'] = 0.03216*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns 
xsec['WJetsPt100'] = 676.3 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt250'] = 23.94 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt400'] = 3.031 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt600'] = 0.4524 #B2G-17-010 / AN2016_480_v5
xsec['WW'] = 118.7 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeVInclusive
xsec['WZ'] = 47.13 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['ZZ'] = 16.523 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['TTH'] = 0.5269 # from XsecDB, NLO
xsec['TTW'] = 0.4611 # from XsecDB, LO
xsec['TTZ'] = 0.5407 # from XsecDB, LO
xsec['TTZl'] = 0.2529 # from McM
xsec['TTZq'] = 0.5297 # from McM
xsec['TTWl'] = 0.2043 # from McM
xsec['TTWq'] = 0.4062 # from McM
xsec['Tt'] = 136.02 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Tbt'] = 80.95 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Ts'] = 7.20/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Tbs'] = 4.16/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TtW'] = 35.83 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TbtW'] = 35.83 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma

#Scaling all HTB signal x-secs to 1pb as agreed with POM, 
#so we have the signal yields scaled to 1pb
xsec['Hptb180'] = 1.#((0.824531)**2/0.683584)*0.75 #interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb200'] = 1.#0.824531*0.75 #was 0.783951 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb220'] = 1.#0.683584*0.75 #was 0.648629 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb250'] = 1.#0.524247*0.75 #was 0.4982015 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb300'] = 1.#0.343796*0.75 #was 0.324766 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb350'] = 1.#0.2312180*0.75 #was 0.2184385 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb400'] = 1.#0.158142*0.75 #was 0.148574 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb450'] = 1.#0.1106674*0.75 #was 0.104141 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb500'] = 1.#0.0785572*0.75 #was 0.0735225 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb750'] = 1.#0.0172205*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb800'] = 1.#0.0130645*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb1000'] = 1.#0.00474564*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb2000'] = 1.#(8.70916e-05)*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb3000'] = 1.#((8.70916e-05)**2/0.00474564)*0.75 #interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt

xsec['HTBM180'] = 1.#((0.824531)**2/0.683584)*0.75 #interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM200'] = 1.#0.824531*0.75 #was 0.783951 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM220'] = 1.#0.683584*0.75 #was 0.648629 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM250'] = 1.#0.524247*0.75 #was 0.4982015 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM300'] = 1.#0.343796*0.75 #was 0.324766 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM350'] = 1.#0.2312180*0.75 #was 0.2184385 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM400'] = 1.#0.158142*0.75 #was 0.148574 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM450'] = 1.#0.1106674*0.75 #was 0.104141 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM500'] = 1.#0.0785572*0.75 #was 0.0735225 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM750'] = 1.#0.0172205*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM800'] = 1.#0.0130645*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM1000'] = 1.#0.00474564*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM2000'] = 1.#(8.70916e-05)*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM3000'] = 1.#((8.70916e-05)**2/0.00474564)*0.75 #interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt

xsec['TTM700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo

xsec['BBM700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo

xsec['X53X53M700left']   = 0.455 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M700right']  = 0.455 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M800left']   = 0.196 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M800right']  = 0.196 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M900left']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M900right']  = 0.0903 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1000left']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1000right'] = 0.0440 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1100left']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1100right'] = 0.0224 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1200left']  = 0.0118 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1200right'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1300left']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1300right'] = 0.00639 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1400left']  = 0.00354 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1400right'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1500left']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1500right'] = 0.00200 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1600left']  = 0.001148 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1600right'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top

xsec['QCDht100'] = 27990000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht200'] = 1712000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht300'] = 347700. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht500'] = 32100. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht700'] = 6831. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht1000'] = 1207. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht1500'] = 119.9 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht2000'] = 25.24 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD

#energy scale samples (Q^2)
xsec['TTJetsPHQ2U'] = xsec['TTJetsPH']
xsec['TTJetsPHQ2D'] = xsec['TTJetsPH']
xsec['TtWQ2U'] = xsec['TtW']
xsec['TtWQ2D'] = xsec['TtW']
xsec['TbtWQ2U'] = xsec['TbtW']
xsec['TbtWQ2D'] = xsec['TbtW']

#4 Tops
xsec['4TM690'] = 1.

# Calculate lumi normalization weights
weight = {}
for sample in sorted(nRun.keys()): 
	if 'BBM' not in sample and 'TTM' not in sample: 
		#print sample, (xsec[sample]) , (nRun[sample])
		weight[sample] = (targetlumi*xsec[sample]) / (nRun[sample])
	else: weight[sample] = (targetlumi*BR[sample[:2]+sample[-4:]]*xsec[sample[:-4]]) / (nRun[sample])
# Samples for Jet reweighting (to be able to run w/ and w/o JSF together!):
for sample in sorted(nRun.keys()):
	if 'QCDht' in sample or 'WJetsMG' in sample: weight[sample+'JSF'] = weight[sample]

#  LocalWords:  nRun
for smp in weight.keys():
	if 'TTJets' in smp:
		for hf in ['_tt2b','_ttbb','_ttb','_ttcc','_ttlf']: 
			weight[smp+hf]=weight[smp]
