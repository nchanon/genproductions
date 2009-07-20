

import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from Configuration.GenProduction.PythiaUESettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.0006),
    comEnergy = cms.double(10000.0),
    crossSection = cms.untracked.double(3490.),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
	processParameters = cms.vstring(
	    'MSEL=0       ', 
            'MSUB(14)=0   ', 
            'MSUB(18)=0   ', 
            'MSUB(19)=0   ', 
            'MSUB(20)=0   ', 
            'MSUB(29)=0   ', 
            'MSUB(11)=1   ', 
            'MSUB(12)=1   ', 
            'MSUB(13)=1   ', 
            'MSUB(15)=1   ', 
            'MSUB(16)=1   ', 
            'MSUB(28)=1   ', 
            'MSUB(30)=1   ', 
            'MSUB(31)=1   ', 
            'MSUB(53)=1   ', 
            'MSUB(68)=1   ', 
	
	'CKIN(3)=300  ! minimum pt hat for hard interactions',
	'CKIN(4)=500  ! maximum pt hat for hard interactions'),
	# This is a vector of ParameterSet names to be read, in this order
	parameterSets = cms.vstring('pythiaUESettings', 
	'processParameters')
	
   

    )
)


gj_filter = cms.EDFilter("PythiaFilterGammaJetWithBg",
    MaxEvents = cms.untracked.int32(2),
    MaxPhotonEta = cms.untracked.double(2.8),
    MaxPhotonPt = cms.untracked.double(22.0),
    MinPhotonEtaForwardJet = cms.untracked.double(1.3),
    MinDeltaPhi = cms.untracked.double(170.0),
    MinPhotonPt = cms.untracked.double(18.0),
    MaxDeltaEta = cms.untracked.double(1.3),
    PhotonSeedPt = cms.untracked.double(5.0)
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string
('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/PYTHIA6_QCDEnrichedpt_300_500_10TeV_cff.py,v $'),
    annotation = cms.untracked.string('QCDEnrichedpt-300-500 at 10TeV')
)

ProductionFilterSequence = cms.Sequence(generator*gj_filter)