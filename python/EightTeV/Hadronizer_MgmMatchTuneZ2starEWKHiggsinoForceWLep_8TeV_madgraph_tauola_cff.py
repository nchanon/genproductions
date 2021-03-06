import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia6HadronizerFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    comEnergy = cms.double(8000.0),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=0         ! User defined processes', 
                        'PMAS(5,1)=4.8   ! b quark mass',
                        'PMAS(6,1)=172.5 ! t quark mass',
			'MSTJ(1)=1       ! Fragmentation/hadronization on or off',
			'MSTP(61)=1      ! Parton showering on or off',
                        'MDME(190,1) = 0    !W decay into dbar u', 
                        'MDME(191,1) = 0    !W decay into dbar c', 
                        'MDME(192,1) = 0    !W decay into dbar t', 
                        'MDME(194,1) = 0    !W decay into sbar u', 
                        'MDME(195,1) = 0    !W decay into sbar c', 
                        'MDME(196,1) = 0    !W decay into sbar t', 
                        'MDME(198,1) = 0    !W decay into bbar u', 
                        'MDME(199,1) = 0    !W decay into bbar c', 
                        'MDME(200,1) = 0    !W decay into bbar t', 
                        'MDME(205,1) = 0    !W decay into bbar tp', 
                        'MDME(206,1) = 1    !W decay into e+ nu_e', 
                        'MDME(207,1) = 1    !W decay into mu+ nu_mu', 
                        'MDME(208,1) = 1    !W decay into tau+ nu_tau'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    ),
    jetMatching = cms.untracked.PSet(
       scheme = cms.string("Madgraph"),
       mode = cms.string("auto"),	# soup, or "inclusive" / "exclusive"
       MEMAIN_nqmatch = cms.int32(5),
       MEMAIN_etaclmax = cms.double(5),
       MEMAIN_qcut = cms.double(23.0),
       MEMAIN_minjets = cms.int32(0),
       MEMAIN_maxjets = cms.int32(2),
       MEMAIN_showerkt = cms.double(0),   
       MEMAIN_excres = cms.string(""),
       outTree_flag = cms.int32(0)    
    )    
)
