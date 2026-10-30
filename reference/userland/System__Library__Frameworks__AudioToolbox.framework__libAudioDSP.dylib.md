# `/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`

iOS 27.2 dyld shared cache image. Version `881.210.0.0.0`. **[DSC]**

## Linked libraries (19)

- `/System/Library/PrivateFrameworks/AudioDSPGraph.framework/AudioDSPGraph`
- `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`
- `/System/Library/PrivateFrameworks/MIL.framework/MIL`
- `/usr/lib/libAudioDSPCore.dylib`
- `/System/Library/PrivateFrameworks/caulk.framework/caulk`
- `/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`
- `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`
- `/System/Library/Frameworks/CoreAudio.framework/CoreAudio`
- `/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/Library/PrivateFrameworks/Espresso.framework/Espresso`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/RemoteProcessingBlock.framework/RemoteProcessingBlock`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking`

## Objective-C: 4 classes, 4 protocols, 55 methods, 26 properties

### Class pages

Every class and protocol, with its methods: [`AudioDSPUplinkSpeechMixer`](../objc/AudioDSPUplinkSpeechMixer_libAudioDSP.dylib.md), [`AudioDSPUplinkSpeechMixerFactory`](../objc/AudioDSPUplinkSpeechMixerFactory_libAudioDSP.dylib.md), [`NSCacheWrapperEntry`](../objc/NSCacheWrapperEntry_libAudioDSP.dylib.md), [`NSObject`](../objc/NSObject_libAudioDSP.dylib.protocol.md), [`NeuralNetCache`](../objc/NeuralNetCache_libAudioDSP.dylib.md), [`RPBServerListener`](../objc/RPBServerListener_libAudioDSP.dylib.protocol.md), [`UplinkSpeechMixer`](../objc/UplinkSpeechMixer_libAudioDSP.dylib.protocol.md), [`UplinkSpeechMixerFactory`](../objc/UplinkSpeechMixerFactory_libAudioDSP.dylib.protocol.md)

### Classes

`AudioDSPUplinkSpeechMixer`, `AudioDSPUplinkSpeechMixerFactory`, `NSCacheWrapperEntry`, `NeuralNetCache`

### Protocols

`NSObject`, `RPBServerListener`, `UplinkSpeechMixer`, `UplinkSpeechMixerFactory`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{AudioStreamBasicDescription=dIIIIIIII},R,N) streamDescription;
@property (TI,R,N) maximumFramesPerSlice;
@property (T@?,R,N) processBlock;
@property (T{AudioStreamBasicDescription=dIIIIIIII},N) streamDescription;
@property (TI,N) maximumFramesPerSlice;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{AudioStreamBasicDescription=dIIIIIIII},R,D,N) streamDescription;
@property (TI,R,D,N) maximumFramesPerSlice;
@property (T@?,R,D,N) processBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{AudioStreamBasicDescription=dIIIIIIII},D,N) streamDescription;
@property (TI,D,N) maximumFramesPerSlice;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (11,004)

First 3,000 of 11,004.
```
[%{public}.*s] AULeanSpatial: headtracker OFF
failed to run blending graph
[%s|%s] Failed to initialize with error code %d
[%s|%s] Updating audio channel layout %s
%25s:%-5d AUDenoise: Initialize.\n
%25s:%-5d Setting property FIRMatrices
[%s|%s] Triangle lookup failed. Unable to complete SoundStage warping.
%25s:%-5d Found the dictionary Weights.
%25s:%-5d Graph is null
[%p] \nKernel Plist AUX code types and assignments
%s:%i initialized
%s:%i create bypass graph
[%p] successfully constructed
[%p] Current input sample rate (%g Hz) not matching NeuralNet sample rate (%g).
[%p] constructed
[%s|%s] Setting tuning warping parameters
%25s:%-5d AUECMIMO::ProcessMultipleBufferLists error - wrong (%u) block size expected (%u)\n
%25s:%-5d EXCEPTION (%d) [topLevelDict_ref.get_cf() == nullptr is false]: \"Missing dictionary: %s\"
[%{public}.*s] using %zu elements from external state storage for %u fractional delay lines (%zu per line, starting at offset %zu)
[%{public}.*s] insufficient scratch for MDF init: need %zu, got %zu
[%p] will construct
%25s:%-5d Failed to set data for property %u (%s)
%25s:%-5d mOutputMaskMode not found, being set to (%u).\n
%25s:%-5d Streaming mode None: no initialization required.
uplink speech mixer failed to create DSP graph - %@
%25s:%-5d Error loading RealCoefficients.\n
%25s:%-5d FFT object failed to Initialize() with block-size %u.
%25s:%-5d Updating parameters
[%s|%s] Failed to compute the ideal RT60 for the given data. Returning empty optional.
[%s|%s] ERROR: ImmersiveRendererData_V1 struct truncated
Failed to set AUSpatialMixer headphone preset
%25s:%-5d SetNoiseEstimator() failed.
[%s|%s] Could not locate an IR file at %s
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"MaxInputChannelCount\"] has invalid value
%25s:%-5d Successfully retrieved forgetting factor Lambda_TC (%g sec.).\n
%s:%i failed to create processing graph model
[%s|%s] error %d while initializing the source extent processor
[%s|%s] Unsupported directivity model: %u
[%s] Reusing cached ATFs, SHbasis, Menc, and beamWeights
%s:%i failed to create bypass graph - %@
failed to migrate AudioUnit assets due to uncaught exception
%25s:%-5d CPMS amplifier model: [ %s ]
[%p] AUReferenceSignal's property list maps orientation \"%s\" to multiple configurations: %s
%s:%i failed to initialize processing graph - %@
[%p] Input size of EmbeddingVector_CF is not expected size (%lu) != (%lu)
[%s|%s] Destructing
mOutputGraphTensor is nullptr in getOutputSize()
%25s:%-5d Failed to retrieve number of beams.\n
%25s:%-5d Failed to retrieve EQ filter length.\n
[ECv6] SetProperty(InitializeIR) rejected: inData=%p inDataSize=%u (expected >=%zu)
[%{public}.*s] AULeanSpatial: headtracker unsupported (error=%d)
%25s:%-5d AUECMIMO: Set iQRD mode.\n
[%s|%s] property %u is not listed as reserved, hence is not going to be intercepted.
[%{public}.*s] engine not initialized
%25s:%-5d Pull failed on input (%u)
[%p] Tried to select a postmask indexed at (%u), but only (%u) masks are available
[%s|%s] Initializing TorqueEngine
[%s|%s] Creating HOA decoders: Input Tag = %u (%s), Output Tag = %u (%s), SphericalGrid = %u
[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] Mic=%u Ref=%u out of bounds (NumMics=%u NumRefs=%u); skipping
[%p] Loading task ID.
[%s|%s] Error: null input or output buffer lists
%25s:%-5d AUECMicRef: ********* Reset begins *********\nAUECMicRef: state variables have finite values (1 if True): %u\nAUECMicRef: ref-signal buffers have finite values (1 if True): %u\nAUECMicRef: EC output buffers have valid values (1 if
%25s:%-5d Successfully parsed the power group descriptions.
[%s|%s] Could not set reverb blend on sc #%u, input element #%u
%25s:%-5d Setting the stream format for the second input bus to match the format of the first bus.
%25s:%-5d Format not supported, output bus %u (format: %s)\n
[%s|%s] [InputElement #%u] Invalid element
[%s|%s] Unsupported normalization in the source extent IR file, Spatializer will ignore source size.
%s:%i cannot process %u I/O channels with %u channel DSP
[%s|%s] Re-allocating alignment delay line: requested delay %u exceeds capacity %u; transition will not be glitchless
[%s|%s] ImmersiveRendererData could not set the distance parameter to 1 for mono input %u, err = %d
[%{public}.*s] initialized MDF convolver for BRIR/LATE (freqDomain=%d, partitions=%zu, channels=%zu, bankMode=%d, stateBytes=%zu)
[%p] NeuralNet is initialized with %u input channels, %u output channels, block size %u.
failed to calculate expected blending graph output frame count
%25s:%-5d Invalid number (%u) of output buses requested. We only support 1–3 buses.
[%s|%s] Disposing input capture file
[%p] NeuralNet's number of input channels (%u) times batch size (%u) not matching AU's number of input channels (%u).
%25s:%-5d Compute engine name set to (%s).
%25s:%-5d AUBeamNF::Initialize (%p)
%25s:%-5d Successfully retrieved number of coefficients (%i).\n
[%p] cannot process %u frames (maximum frame size is %u)
[%s|%s] invalid output channel layout %d
%25s:%-5d The top-level parameter data structure is not saved internally! Instead, you should query specific AU properties individually.
%25s:%-5d Successfully parsed all the per-speaker OL displacement params.
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve BlockSize.\"
%25s:%-5d Failed to retrieve beam elevation.\n
SpatialBalance registration failed
[ECv6] DrainPendingIRs: mic=%u pending size %zu is not a multiple of refChannelsToUse=%zu; skipping
[%p] cannot process %u output busses (expected output bus count is %u)
[%s|%s] Set SoundStage Parameters
[%s|%s] Preset exported to %@
%25s:%-5d Successfully retreived FFT2Mel.
[%p] failed to set DSP graph property %s
%25s:%-5d Initialization failed. Setting the AU to bypass mode.
%25s:%-5d Successfully retrieved DeltaFeature (%u).\n
%25s:%-5d Ch %d, Set up for OpenLoopDisplacement
%25s:%-5d AUBeam2::ReverseMicChannelFlag is set to 1 (AU input mic order {front/side,back}, will not flip mic order for BF kernel ) 
%25s:%-5d Graph source generation failed
[%p] AUReferenceSignal's property list \"Configurations\"[%u] has invalid \"Gains\" value
processing preflight gave invalid number of frames to process!
[%{public}.*s] LSSource::initialize: insufficient scratch buffer: got %zu elements, need %zu elements
[%s|%s] Exp Decay Coeff: %f.
[%s|%s] AUSM_VERBOSE|ReverbSendGains=%s
%25s:%-5d kAUEndpointVAD3Property_EventHandler is write-only.
[%s|%s] ImmersiveRendererData did not set optional feature dictionary.
%25s:%-5d AUSpeakerProtectionV3 bypassed!
[%s|%s] ImmersiveRendererData: kImmersiveRendererType_Unknown used for input #%u. Fallback to object.
LoudspeakerController battery tracking is enabled - telemetry input must be present
AUECRMGS: Reset.\n
[%s] Initialisation time = %.2f ms
[%s|%s] ImmersiveRendererData failed to enable input %u, err = %d
[%s|%s] Too many parameters
%25s:%-5d AUBeam2: Error: inFramesToProcess != GetMaxFramesPerSlice(), inFramesToProcess = %d, GetMaxFramesPerSlice() = %d
uplink speech mixer failed to create DSP graph remote processing block host - %@
[%s|%s] Mismatch in critical distance for %s reverb; early = %.1f, late = %.1f
ControlFreak registration failed
Register NoiseGate
%25s:%-5d Getting property info for SubbandDOA_CF failed (prop id: %d).
[%s|%s] Unsupported reverbProcIndex %u on sc #%u, input element #%u
Failed to set Music EQ Dialogue dictionary
[%s|%s] error %d setting stream formats on %s; disabling processing
[%s|%s] Custom Bypass Matrix was not loaded; invalid dictionary
%25s:%-5d AUNeuralNetRES: (OutputSignals) is NOT finite: (%u)
%25s:%-5d mFadeTime_ms: %f\n
%25s:%-5d Successfully retrieved DirectionalModelType (%d).\n
%s:%-5d Number of Output Elements provided is greather than the Maximum supported.
%25s:%-5d SetVideoMode was set on an SNR estimator that does not support it.
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"OutputChannelCounts\"] has invalid value
%s: error %d setting the maximum frames per slice = %u for %s
%25s:%-5d EXCEPTION (%d) [inState.size() != outState.size() is false]: \"Input state %s size (%zu) not matching the output state size %s (%zu).\"
failed to set spatial metadata with status %d
[ECv6] SetProperty(InitializeIR) rejected: AU already initialized
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"OutputChannelLayouts\"][%u] has invalid value
%s: disposing of %s
%25s:%-5d Number of processed samples exceeds allocated buffer size.
[%{public}.*s] external span size mismatch for FD coefficients (have %zu, need %zu)
%s:%i failed to set processing graph neural net property list
%25s:%-5d AUECMIMO: AOPMode detected (non-realtime logging).\n
%25s:%-5d AUNeuralNetVAD: (OutputSignals) is NOT finite: (%u)\n
%25s:%-5d Invalid number (%u) of output buses requested. We only support 1–2 buses.
%25s:%-5d GetMaxFramesPerSlice(): %u\n
%25s:%-5d AUSeparate: Successfully initialized.\n
[%s|%s] ConvertOutputData ERROR: result = %d
[%s|%s] error %d while initializing the NF processor
[%s|%s] BiNeural Successfully Initialized
AUSM_INIT_EVENT
%25s:%-5d Preparing a NeuralNet from topLevelDict.
[%s|setProperty] (scope=%u, element=%u): %s: invalid size %u, expected %u
%25s:%-5d EXCEPTION (%d): \"Run time error: %s\"
[%s|%s] ImmersiveRendererData failed to set the spatialization algorithm for input %u, err = %d
%25s:%-5d AUBeamNF: Error: Could not open post EQ file %s
[%{public}.*s] process error, not enough output channels configured
[%s|%s] ERROR: cannot process with %d output channels != 2
[%s|%s] Creating the output capture file: %s
%25s:%-5d Failed to initialize internal audio units.
[%p] failed to process because DSPGraph is null
%25s:%-5d AUSpeakerProtectionV3::SetProperty - Telemetry data order. Could not be fully parsed (invalid data?).\n
%25s:%-5d ERROR: We have not been configured with a LUT system; we cannot initialize properly and will process in soft bypass.
%25s:%-5d cached BNNS IR '%s' is unreadable (%s) -- removing stale entry (likely PROTECTION_CLASS_F key purge after reboot)
%25s:%-5d Conditional target prior not set to (%f), it remains at the current value (%f). Valid range is [0, 1].\n
Init: Failed to set AUDSPGraph output stream format
[%s|%s] Initializing surround filters
[%p] The NeuralNetBNNSData_CF passed to SetProperty is not CFDictionaryRef type or it's null.
%25s:%-5d  Volume curve steps must match
%25s:%-5d Block Size for DFT must be divisable by 2**4! Setting AU in Bypass mode.\n
[%s|%s] inNumIRProcessors cannot be zero when creating an instance of this class
%s:%i Number of input channels in the plist (%u) is different from the number of output channels in the plist (%u)
%s: WARNING: AUXTC file at %s is invalid (need 4ch, 48kHz, <=256 frames)
%25s:%-5d Failed to fully parse the %s plist entry for channel %i.
AUAGCV2 calibration meter: %2.1f dB
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Alpha from dictionary Activation.\"
[%s|%s] SetExclusionZones from dictionary failed with error %d
[%{public}.*s] HRIR processing failed for source #%u: %d
%25s:%-5d Successfully retrieved beam elevation (%0.2f).\n
Failed to configure graph
[%s|%s] Invalid sample rate and/or order
[%s|%s] Resetting ScottyLite
%25s:%-5d NeuralNetVAD: Loading WaitFrames from topLevelDict.
[%s|%s] GD: Group %u not found
%25s:%-5d Input MCLPOutSignals buffer expected with (%u) channels.
[%{public}.*s] zero-padded partition %zu, channel %zu (%zu/%zu samples)
%25s:%-5d Failed to set beam selection mode: %@
%s: Virtual Surround Tool XTCIR file written to: %s
[%p] failed to initialize - channel map element %d is larger than number of input channels
%s:%-5d Input Format is Invalid.
%s:%-5d Unsupported Algorithm Core Type Provided
[%{public}.*s] BothEars mode requires 2 coefficient channels, got %zu
%25s:%-5d EXCEPTION (%d) [(nBytes * mNumberBuffers) > AllocatedBytes() is false]: \"\"
%25s:%-5d CADSPUtility:%s:%d: VBAP error, Delaunay triangulation issue
blending preflight gave invalid number of frames to process!
[%s] Async synthesiser initialisation dispatched (generation %u)
%25s:%-5d AUDenoise: (InputSignals, EchoEstimates) is NOT finite: (%u, %u)\n
uplink speech mixer failed to initialize DSP graph - %@
[%s|%s] Error creating neural network - error loading plist file: %s
%25s:%-5d AUBeam2: Error: Number of unique bands is zero, won't dump post EQ
%25s:%-5d Limit wind boost ref is channel %i
[%p] Tried to select a model indexed at (%u), but only (%u) models are available. A new model will not be selected and AUNeuralNet will run as if bypassed (until a new model is selected).
%25s:%-5d Output Sensitivity: %f
%25s:%-5d AUDenoise: (OutputSignals, PMWFLeeOut) is NOT finite: (%u, %u)\n
%25s:%-5d CLSPKernel_v5::Reset
%25s:%-5d CADSPUtility:%s:%d: HOA Warning; initializing a HOA instance with order = %d > 10
%25s:%-5d AUECSUMO: Reset.\n
[%{public}.*s] Expected %zu frames but got %u frames
[%{public}.*s] late processor initialized with external state (%zu bytes)
%25s:%-5d Override SpCl Property with defaults clsp_caltemp %f
[%s|%s] ImmersiveRendererData could not set the source mode to ambience bed for input %u, err = %d
********* Reset begins *********\nref-signal buffers have finite values (1 if True): %u\nEC output buffers have valid values (1 if True): %u\n
[%p] failed to initialize - sample rates of BackMic input bus and main output bus must be equal
%25s:%-5d The host requested latency before the real value is available!
[%s|%s] started
[%s|%s] Resetting
%25s:%-5d EXCEPTION (%d): \"mmap of bnns IR file (%s) failed with error (%s)\"
%25s:%-5d CPMS power budget '%s' is %f
[%s|%s] Applied source mode = %u based on defaults write 
[%s|%s] Setting CounteractRotationShader = %s
[%s|%s] Deleting upmixer
%25s:%-5d Path to compiled IR file: %s
[%s|%s] ImmersiveRendererData: failed to create export file %s
%25s:%-5d AUDistance: (OutputSignals) is NOT finite: (%d)
[%s|%s] SoundStages found to have different number of parameters.
%s:%i failed to load 'AUNeuralNet' preset
[%s|%s] SetParameter failed, err = %d
[%s|%s] SetExclusionZones from array failed with error %d
%25s:%-5d EchoEstimates cannot be NULL when Beam selection is not Off.\n
%25s:%-5d AUECMIMO: filter (readout) length is set to %u (%u) samples.\n
[%s|%s] Unexpected all-ASC group. Not Implemented.
%25s:%-5d Requested ConvoyAdaptiveDisplacement but ParameterUpdaterConfig is not valid
[%{public}.*s] auto-calculated %zu partitions from %zu TD samples per channel
[%{public}.*s] AULeanSpatial: build version 0x%x
%25s:%-5d Successfully retrieved Kalman observation std (%g).
%25s:%-5d SpatialProbabilityBase: Prior probabilities not set. Conditional target prior (%f) should be in range [0, 1].\n
[%{public}.*s] provided with %zu output channels but current bankMode (%u) needs %zu channels
%25s:%-5d External CDR is not used in the current mode. Current mode is (%d)
[%p] initialized
%25s:%-5d Successfully parsed the EnableDisplacementControl param: [ %s ]
%25s:%-5d BeamFarfieldEQ dictionary not present in plist.
%25s:%-5d Error in SetNoiseEstimator(): %s (%s)\n
[%p] disposed mTimeFreqConverterInputDelayed
%s:%i failed to set processing graph denoise delay parameter
[%p] Loading block size from plist.
[%p] Setting SPL attack time: %f, SPL attack constant: %f, SPL release time: %f, SPL release constant: %f,SNR attack time: %f, SNR attack constant: %f
%25s:%-5d BNNSGraphCompileFromFile failed with CAException %d: %s.
[%s|%s] NeuralRAD Successfully Initialized
[ECv6] DrainPendingIRs: mic=%u refChannelsToUse=%d; skipping
%25s:%-5d AUBeamNF: Error: Beam object not initialized, won't dump post EQ
%25s:%-5d Successfully parsed all %lu the per-speaker CL params.
[%s] kAUParametricProcessorV2Property_HopSize being set after AU was initialized
[%s|%s] ImmersiveRendererData failed to set the attenuation law for input %u, err = %d
[%p] Using legacy block processor with delay = %d samples.
[%p] input format not supported
%25s:%-5d CPMS power gain limit is %f dB
[ECv6] SetProperty(ECIR) rejected: inData==nullptr (mic=%u)
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Gains\"][%u][\"Input\"] has invalid value
%25s:%-5d graph size is %zu bytes
[%{public}.*s] FD coefficient size mismatch (expected %zu, got %zu)
%s:%i Not bypassed at initialization - activate smooth transition
%s:%i failed to set processing graph %s input delay parameter - %@
%25s:%-5d Binding buffer for output state %s
%25s:%-5d Input format is %s
%25s:%-5d Unknown exception!
[%s|%s] AUSM latency is increased to %u (samples)
%25s:%-5d No valid .plist file set, going to passthrough mode and bypassing LoudnessWarrior\n
%25s:%-5d Unknown status thrown: %d\n
[%{public}.*s] using init scratch from inScratch tail (%zu floats, %zu bytes, offset=%zu DataType elements)
[%s|%s] Found user defaults %s = %u
[%p] NeuralNet expects input block size %u, and we received %d.
%25s:%-5d Successfully retrieved number of input channels (%u).
%25s:%-5d Steering vector to be loaded from a plist.
[%{public}.*s] source(inactive): initialized at %uHz
[%s|%s] HOA reverb order (%u) can not be greater or equal to input HOA order (%u)
%25s:%-5d NeuralNetVAD: Loading threshold from topLevelDict.
%25s:%-5d Spatial capture graph source generation: bad number of outputs provided: %u
[%p] AUNeuralNetVADV2: Resetting state variables. Cleanup() started.\n
%s:%i NeuralNetPresetPath is overriden to %s
[%s|%s] Not initializing TorqueEngine
[%s|%s] AUSM_VERBOSE|DirectIRWeights[%u]={%s}
[%s|%s] ERROR: ImmersiveRendererData_V1: Inconsistent workflow: IRD version %u ≠ 1
%25s:%-5d AUSeparate: Initialize.\n
[ECv6] LoadPendingIRsFromDictionary: zero-valued header (NumMics=%u NumRefs=%u FilterSize=%u)
[%p] Low Delay block processor not supported for process block size (%s) > Model block size (%u)
%25s:%-5d The CFDictionaryRef passed to SetProperty is null.\n
%25s:%-5d SpCl property data is null
%25s:%-5d CADSPUtility:%s:%d: VBAP Error; Triangle lookup failed
%s:%i DereverbPresetPath is overriden with an empty string.
%s:%i bypass graph is null
%25s:%-5d Profile vector is not present in the dictionary.
%25s:%-5d Setting property EnableSubbandDOACalculation failed (prop id: %d).
%25s:%-5d BNNSGraphCompileFromFile fallback failed with CAException %d: %s.
[%s|%s] Could not set directivity index to %u on sc #%u, input element #%u
[%{public}.*s] will zero-pad last partition(s) with %zu samples
[%s|%s] Failed to find valid index for SoundStage with enum = %d
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"InputChannelCounts\"] has invalid value
[%s|%s] Could not disable the PP late reverb: err = %d
%25s:%-5d will try to initialize\n
%s:%i --
[%s|%s] Unexpected nullptr track
[%{public}.*s] null input pointer for source %u
[%{public}.*s] BothEars mode requires 2 output channels, got %zu
[%p] Processing error (%d)
[%s|%s] Error %d setting divergence position range to -1
AUAGCV2 VAD created sample rate converter
%25s:%-5d Supported render modes:
%25s:%-5d AUNeuralNetRES: Reset.\n
%25s:%-5d AUBeamNF: Error: inFramesToProcess != GetMaxFramesPerSlice(), inFramesToProcess = %d, GetMaxFramesPerSlice() = %d
%25s:%-5d sample rate of input buses doesn't match
%s:%i failed to initialize blending graph - %@
[%s|%s] Could not reconfigure auto mode %s late reverb: error %d
Closed loop thermals enabled but IV buffer missing or not correct. Disabling CL thermals.
[%s] Deconstructing (ID %p)
[%s] Unsupported hop size - hop size must be 64 or 128
%25s:%-5d Could not fully parse gain-link group information. All speakers will be in group 0.
%25s:%-5d Block size is not supported! Setting AU in Bypass mode.
[%{public}.*s] LSBank: window start sample beyond end of filter
[%s|%s] Number of channels in stream format changed
%25s:%-5d AUNeuralNetRES: Cleanup().\n
%25s:%-5d ---
%25s:%-5d Ignoring orientation update with unsupported value %u
%25s:%-5d Successfully retrieved sample rate (%g Hz).\n
[%s|%s] Warning: scheduling parameters while the parameter smoothing is not set to scheduled parameters.
%s: error initializing %s
%25s:%-5d AUBeamNF: Error loading post EQ file at %s
[%s|%s] ImmersiveRendererData failed to set the stream format for input #%u, err = %d
[%s|%s] Input Element #%u for ASC #%u does not exist
[%s] Deconstructing
%25s:%-5d Sample rate not provided in tuning dictionary
%25s:%-5d Current elevation not set to (%f), it remains at the current value (%f). Elevation must be in range [-90, 90].\n
%25s:%-5d Ch %d, Convoy calibration parameters out of range or not Coff < CMin < CMax. Defaulting to Open loop displacement. CMax=%f, CMin=%f, Coff=%f
[%p] Successfully retrieved sample rate %g Hz.
%s:%i AUNeuralNet registration failed
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"BlockSize not loaded.\"
MetadataDNNVAD:%s:%d: couldn't initialize - %@
%25s:%-5d AUSpeakerProtectionV3::SetProperty - IgnoreTelemetry. Set as: [ %s ].\n
NeuralNetGetTemporaryDirectoryPath: TMPDIR not set, using NSFileManager.temporaryDirectory: %{public}s
%25s:%-5d SetSubbandDOACalcuationEnabled failed, subband DOA calculator is already initialized and this value cannot be changed.
successfully retrieved spectral profile sample rate (%u Hz)
%s:%i NeuralNetModelNetPathBase is overriden to %s
%s:%i non-AMX/SME iOS device: HQ model not supported
%s: Error: Virtual Surround Tool XTCIR file could not be written to: %s
%25s:%-5d Subband DOA is only used for the DOA mode. Current mode is (%d)
%25s:%-5d Closed loop checks Ch %d passed: mCLParams.size=%d, nKern=%d, SpClProps.size=%d
[%s|%s] Could not remove reverb by setting reverb blend to 0 for group id = %u, err = %d
%25s:%-5d Loading ECOutScale from topLevelDict.
%25s:%-5d BestBeamInEcho set to a value greater than number of beams. Setting it to mNumBeams-1.\n
%25s:%-5d Bass or treble BQs not defined correctly for sample rate of %.0f!\n
[%s|%s] Triangle containment not found for coordinates %f, %f, %f
%25s:%-5d CircularModels: Kappa not set. Input length (%lu) and internal length (%u) do not match.\n
[%s|%s] (scope=%u, element=%u): invalid element (property = %u)
ParseBlob() failed with exit code %d
[%{public}.*s] using external state memory (%zu bytes total)
[%{public}.*s] will zero-pad %zu samples
[%s|%s] Resetting FDN
[%s|%s] [InputElement #%u] Setting audio channel layout %s
%s: null dictionary ref for %s
%25s:%-5d Initialize BeamNFN object with: sample rate = %f, transform size = %d, frame size = %d, number of beams = %d
[ECv6] LoadPendingIRsFromDictionary: unsupported FormatVersion=%u (expected 1)
[%p] audio captures are enabled with name \"%@\"
%25s:%-5d Initialize called with properly set BeamFormerCoeffs plist.\n
%25s:%-5d Invalid bass EQ sizes: BQ vectors must be same length\n
%25s:%-5d DirectionalModelShapeParamer not found, being set to (%g).\n
%s:%i ---
%25s:%-5d Ending initialization.
%25s:%-5d preflight gave invalid number of frames to process!
[%p] NeuralNet is initialized with %u input channels, %u output channels, block size %u, and batch size %u.
[%p] failed to create graph model - %@
[%{public}.*s] uninitialized
%25s:%-5d AUSpeakerProtectionV3:: Found additional pilot tone params %s, applying to scope
ToneMeister registration failed
[%s|%s] Biquads not removed - lock not acquired
%25s:%-5d NeuralNetVAD: Loading DirectionalModelType from topLevelDict.
%25s:%-5d Set SpeakerCalibration property: Applying calibration data on top of SpTS. Not as intended.
[%p] failed to initialize - sample rates of M1 input bus and main output bus must be equal
%25s:%-5d Failed to set new FIR matrix on active kernel: %s (err=%d)\n
[%s|%s] Error with upmixer initialization with error code %d
%25s:%-5d AUDereverb: ********* Logging ends *********\n
[%s|%s] ImmersiveRendererData failed to set the attenuation law, err = %d
Failed to create austrip plist
Failed to set AUSpatialMixer factory preset
[%s|%s] Neural network has valid %u output channels; FOA channels will be predicted
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary Weights.\"
[%s|%s] TuningWarperParameters = %s
%25s:%-5d mBlockSize: %u\n
%s:%i processing graph is null
[%p] NeuralNet0 blockSize (%u) and NeuralNet(%u) blockSize (%u) do not match
[%{public}.*s] source(inactive): setting up HRIR processor
[%s|%s] Tuning Parameters dictionary structurally invalid. Failed to set, returning.
%25s:%-5d Spatial capture graph source generation: bad block size provided: %u
%25s:%-5d MCLPoutSignals cannot be NULL. It is a required input\n
[%s|%s] Using default input channel layout tag = %u (%s)
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"OutputChannelCounts\"][%u] has invalid value
[%s|%s] finished
[%s|%s] BiNeural loaded with %u inputs and %u outputs
[%s|setPropertyDictionary] (scope=%u, element=%u): unsupported number type for dictionary entry %u
%25s:%-5d BypassMicIndex set to a value greater than number of input mics. Setting it to mNumMics-1.\n
%25s:%-5d NeuralNetVAD: Loading UseDirectionalMode from topLevelDict.
%s:%i simulator root is \"%s\"
%25s:%-5d Successfully retrieved DirectionalTargetElevation (%g).\n
%25s:%-5d MIL2BNNS secondary cache file '%s' %s
[%s|%s] only supporting octave band resolution. Returning empty optional.
SetProperty( kAudioUnitProperty_DspLibDictionary ) Error: data did not decode to a dictionary property list\n
Register AUNeuralNet
VAD autocorrelation block size is %d
AudioUnitSetProperty: inDataSize == 0
[%s|%s] Can't compute the intermediate parameter value for parameter = %u, element = %u
[%s|%s] ImmersiveRendererData_V2 ingestion has begun
Registering internal AUs
Unknown AUThreadSafeList event type
[%p] Did not find model named (%s)...
[%s|setProperty] (scope=%u, element=%u): %s = %s (not changed)
%25s:%-5d Setting property BeamformerCoeffs (prop id: %d).
[%s|%s] Room Congruence is turned off. Returning a valid result with an indicator of the feature being turned off.
%25s:%-5d Size of delay line %d
%25s:%-5d Failed to set graph property for mic selector result: %@
%25s:%-5d CADSPUtility:%s:%d: HOA Error; VBAP object was not initialized
%25s:%-5d Successfully retrieved profile vector (length %i).
%25s:%-5d mOutputBuffer size is %u
%25s:%-5d No Closed Loop inputs: numberInputBufferLists=%u, inputBufferList[1]=%p
[ECv6] DrainPendingIRs: mic=%u setMainIr rejected a %zu-sample-per-channel import that passed the length check
%u frames, %u bytes/frame, expected %u-byte buffer; inInputBufferLists[%u].mBuffers[%u].mDataByteSize=%u; kAudio_ParamError
%25s:%-5d CADSPUtility:%s:%d: HOA Error; Inconsistent vector size
%25s:%-5d Retrieved property data for property %u (%s)
%25s:%-5d AUBeamItTD: (InputSignals, EchoEstimates) is NOT finite: (%u, %u)
%25s:%-5d We are all-open loop, or this device does not use SpTS for speaker calibration. MG not queried.
%25s:%-5d Ch %d, Using open loop kernel
[%s|%s] Could not enable the scene reverb on scene component = %u, input = %u, err = %d
[%{public}.*s] allocated internal output delay buffers (%zu samples)
%25s:%-5d AUBeam2: Error: Failed setting diffraction filter and post EQ
  from %s, processmultiple err: %d
[%p]  %c
%25s:%-5d Steering vector is not used in the current mode. Current mode is (%d)
%25s:%-5d AUHearingLossCompensator::Initialize()\n
[%p] noise SPL is %s
%25s:%-5d Identified Output Tensor: %s
%25s:%-5d Part AUSpeakerProtectionV3::SetParameter(%d): %f -> %f\n
[Room Congruence] %s: Room configuration invalid - underlying CF object is nil.
[%s|%s] failed to create neural network output SRC with error code %s
%25s:%-5d Bad beam direction string: '%s'
%25s:%-5d AUBeamNF::DumpPostEQ (%p)
[%{public}.*s] Calling convolver with unsupported amount of samples (%u)
[%s|%s] Zero padding HRIRs for MagLS call.
%25s:%-5d Could not fully parse the EnableCPMSClosedLoopControl param. Will use the default.\n
%25s:%-5d Successfully retrieved input data type (%s) for Layer %zu.
%25s:%-5d AUBeam2: Error: Could not read diffraction filter file %s
%25s:%-5d CADSPUtility:%s:%d: VBAP Error; Triangle lookup error
%25s:%-5d ERROR: Failed to uninitialized internal AU.
%s:%i metrics reporter created
[%p] Error[%d] pulling input from bus 1
%25s:%-5d AUBeamNF: Error loading diffraction filter file at %s
[%p] failed to initialize - sample rates of M4 input bus and main output bus must be equal
successfully retrieved spectral profile vector (length %u)
%s:%i simulator root is unknown
[%p] output format is not valid
[%s|%s] Reusing existing directory for capture: %@
%25s:%-5d Failed to instantiate internal audio units.
[%s|%s] Filter parameter changes were not signficant; filters will not be recalculated
[%{public}.*s] using external output delay buffers (%zu samples)
[%s|%s] Biquad latency not calculated - lock not acquired
[%s|%s] repeated call, suppressing logs for properties that do not change
%25s:%-5d AUDereverb: Initialize MCLP Classes.\n
%25s:%-5d EXCEPTION (%d) [(mInputSize != mNumMelBands*2) is false]: \"mInputSize is wrong.\"
%25s:%-5d Safe limit %f > thermal limit %f. Setting Safe limit = thermal limit.
[%s|%s] Cleanup was not done appropriately (1)
Register AUDSPGraph
VolumeTaper registered successfully
%25s:%-5d CADSPUtility:%s:%d: Diametrically opposed speakers; No need to generate convex hull
[%p] TaskID set to (%s).
%25s:%-5d NeuralNetRES: Loading ECleeScale from topLevelDict.
%25s:%-5d Successfully retrieved input name (%s).
%25s:%-5d CombinedProbabilityMode not found, being set to (%g).\n
[%s|%s] One or more of the chosen IR Presets does not contain room congruence data or the data is corrupted.
[%s|%s] Toggling to OBHD filters
[%s|%s] ImmersiveRendererData could not clear reverb blend on input #%u, err = %d
AUECRMDF::Init warning - tried to set mBlkSize: (%u), but forced mBlkSize to (%u)\n
[%p] Loading sample rate from plist.
[%s|%s] AUSM_VERBOSE|CombinedReverbSendGains=%s
%25s:%-5d Output OutputSignals buffer expected with (%u) channels.
[%s|%s] NeuralNet initialization using plist with assumed base path failed with CAException %d: %s.
%25s:%-5d  CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own
[%p] Creating NeuralNet model
%25s:%-5d Failed to set crossfade parameter for %s beam (overrides: %d): %@
%25s:%-5d Unable to get sample rate
%s:%i set CoreAudio reporter IDs to internal reporter - %s
[%s|%s] invalid output scope element = %u (property = %u)
%25s:%-5d Dictionary file not present on disk!
%25s:%-5d AUBeamNF::ApplyParameterValues (%p)
Failed to open propstrip file
[%p] NeuralNet expects %u output channels, and we received %u.
%s: error %d uninitalizing %s
%25s:%-5d Construct MIL2BNNS.
%25s:%-5d Using speaker gain-link grouping from the plist: [ %s ]
%25s:%-5d EXCEPTION (%d): \"Unsupported LayerType.\"
%s: Temp directory string is empty
[%s|%s] Neural transcoder loaded with %u inputs and %u outputs
%25s:%-5d Number of channels on the input bus in not matching the expected number of channels (%u).\n
uplink speech mixer maximum number of frames per slice must be greater than zero
AUBuffer throwing bad_alloc
%s:%i update local parameter state before creating the processing graph
[%{public}.*s] cannot create source with ID %u - already in use
failed to flush \"%s\"
IV input format not SInt16 or Float32 - unsupported
Failed to set parameter %d
[%{public}.*s] scratch buffer too small
[%s|%s] ImmersiveRendererData: Could not configure Object renderer type to %u, input #%u, err = %d
[%s|%s] Unsupported index: %u
%25s:%-5d SetSNREstimator() failed.
[%s|%s] Biquad dictionary invalid
%25s:%-5d LayerDescriptor for layer %zu not found, using default fully connected layer.
[%p]  AuxSymbolVals %u 
[%p] disposed mTimeFreqConvertersOutput[%d]
[%s|%s] AUSM_VERBOSE|DirectGrid #%u: %s
[%s|%s] ERROR: ImmersiveRendererData_V2 byte size inconsistent
[%s|%s] ERROR: cannot process with %d output channels != %d
%25s:%-5d Found a %zu-element (%gms) reverb tail for the %gHz sample-rate.
%25s:%-5d CADSPUtility:%s:%d: HOA Error; Incorrect order
[%p] NeuralNet expects %u input channels, and we received %u.
[%s|%s] Clipping RT60 to max value: %f
%25s:%-5d Initialization failed, top level plist is not set.
%25s:%-5d Failed to set SelectBeamsFrom parameter: %@
%25s:%-5d Preparing EspressoV2 NeuralNet implementation.
[%s|%s] Mismatch in diffuse field power for %s reverb; early = %.1f, late = %.1f
Failed to set bypass TM dictionary property
%s:%i bad outMatrix num cols
[%p] Successfully retrieved block size %u.
[%p] Successfully retrieved block size (%u).
%25s:%-5d InputSignals cannot be NULL. It is a required input\n
%25s:%-5d EXCEPTION (%d): \"Unsupported input data quantization type for Quantization (%u).\"
%25s:%-5d param %i not found in graph
%25s:%-5d PilotAmplHi limited to %f
%s:%-5d Could not retrieve blocked mic profile data. Will use default\n
[%s|%s] AUSM_VERBOSE|PostProcReverbSendGains=%s
%s:%i DereverbPresetPathOverride is set to null and thus removed
%s:%i failed to get processing graph denoise delay latency
[%s|%s] invalid initialization parameters
%25s:%-5d AUECMIMO: Successfully initialized.\n
%25s:%-5d AUECSUMO: ********* Using the initialized window *********\n
[Room Congruence] %s: IRData User Data invalid - arrays should have the same number of elements.
%25s:%-5d Successfully retrieved bias data (%g) at index (%zu).
%25s:%-5d Sample rate for NNRES is not supported! Setting AU in Bypass mode.\n
%25s:%-5d Failed to set beamformer coefficients, setPropertyError = %@
%25s:%-5d Successfully retrieved implementation type (%s).
%25s:%-5d AUBeamNF: Error: Could not open diffraction filter file %s
%25s:%-5d MIL2BNNS Destructor Bgein.
%25s:%-5d Successfully retrieved coefficients data (%g) at index (%u).\n
%25s:%-5d CADSPUtility:%s:%d: VBAP error; Delaunay triangulation issue
%s:%i failed to set processing graph neural net path override
[%p] Input size of EmbeddingVector  (%lu) is not equal to the the expected size  (%lu).
[%s] Async synthesiser initialisation complete (generation %u, %.2f ms)
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"NumContextFrames not loaded.\"
%s:%i AUBase::SaveState didn't produce valid dictionary?
[%s|%s] Could not set the headphoneVirtualise to %s on group id = %u, err = %d
VAD sparsity block size is %d
%25s:%-5d Setting the property PropertyIDs::DistanceEstimatorNeuralNet
%s:%i will create metrics reporter
[%s|%s] Resetting STFTUpmixer
[%s|%s] ERROR: ImmersiveRendererData_V2 parsing metadata config failed: %s
[%p] \nKernel Plist NumFreqs %u
[%s|%s] Could not set global property %@ from the property dictionary. Error %u
%s:%i Error %i while restoring state
[%s|%s] mixing time computed as %d
[%s] Operating in full 3D mode
%s:%i loading from %s failed
[%s|%s] (scope=%u, element=%u): setting property failed with err = %d (property = %u)
[%s|%s] error %d while initializing the source extent processor for internalized
[%{public}.*s] initialized (filterLength=%u, numOutputs=%u, xFadeLength=%u, maxBlockSize=%u, externalStorage=%s)
%25s:%-5d shared mmap of BNNS IR file (%s) failed: %s; retrying MAP_PRIVATE (model pages will be charged to this process)
%25s:%-5d BNNSGraphCompileFromFile fallback failed with unknown exception.
[%{public}.*s] initializing at %uHz, %lu-bits, bankmode=%u, max pull size=%zu, max push size=%zu 
%25s:%-5d Check input format\n
[%s|%s] MC: Group %u not found
[%s|%s] Failed to compute triangulation.
[%s|%s] Resetting ScottyUpmixer
[%s|%s] Setting target latency to %u
%25s:%-5d Bad channel selection %i
[%s|%s] Exiting with err = %d
%25s:%-5d Loading KalmanObservationStd from topLevelDict.
%25s:%-5d ExternalSourceProbability is not used in the current mode: (%d, %d)
%25s:%-5d MIL2BNNS constructed.
%25s:%-5d MIL2BNNS Deallocating mGraph.data from BnnsIR
%25s:%-5d Could not fully parse the EnableThermalControl param. Will use the default.\n
[%s|%s] Setting low crossover, inFC = %f, inOrder = %u
AU latency is equal to the processing graph latency
%25s:%-5d Ch %d, Convoy calibration parameters within range
[%s|%s] EABL ingestion: Mismatch between the configured number of channels and the actual number of channels given on the call
Failed to create AUDSPGraph instance
%25s:%-5d Internally set the forgetting factor as (%g).\n
%s:%i load dictionary from %s
[%s|%s] Uninitializing STFTUpmixer
%25s:%-5d AUBeamItFD: (InputSignals, EchoEstimates) is NOT finite: (%u, %u)
%25s:%-5d Using defaults write logging level: %d
[%s|%s] Error creating neural network - all channels are LFE, please check channel labels and/or distances
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"OutputChannelLayouts\"] has invalid value
%25s:%-5d EXCEPTION (%d) [mOutputSize != mNumFFTBins is false]: \"NeuralNet output size (%u) is not matching the number of FFT bins (%u).\"
We were initialized with %lu kernels (and for %u channels), but are receiving %u channels of audio. These should all have matched; applying 20dB attenuation to this frame.\n
[%{public}.*s] insufficient state storage for MDF convolver: need %zu bytes, got %zu
%25s:%-5d %s camera direction (%u): %s (%f)
[%p] Initialize AU
[%s|%s] Constructing
[%s|%s] No direct sound
[%s|%s] EABL ingestion: inPullSizeThisTime = %u, timestamp = %f
[%s|%s] Only Input ACL can be set - output is always mono
[%s|%s] Reinitializing shared buffers. immediateUpdate = %s, fftParams {.numOutputs, .numFFTSubFilters, .partitionLength}: hrtfParams = {%u, %u, %u}, sceneBusParams = {%u, %u, %u}, postProcBusParams = {%u, %u, %u}, combinedBusParams = {%u, 
%25s:%-5d Done
%25s:%-5d Successfully retrieved sample rate (%g Hz).
%25s:%-5d Run processing once to prewarm the filters.
%25s:%-5d EXCEPTION (%d) [state_ref.get_cf() == nullptr is false]: \"Missing dictionary (%s).\"
%25s:%-5d rename to secondary cache '%s' failed: %s (caching skipped)
[%s|%s] ImmersiveRendererData_V1: Error during common configuration, err = %d
%25s:%-5d %s param %u: val=%f
%s:%i failed to set processing graph neural net preset
%25s:%-5d EXCEPTION (%d) [outputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve OutputName.\"
[%{public}.*s] initializing processor at %zu samples, bank mode %d
%25s:%-5d Input and output audio formats don't match.
%25s:%-5d CPMS amplifier model: [ default ]
%25s:%-5d Could not fully parse the power amplifier efficiency model. Will use the Dummy model.\n
%25s:%-5d AUEndpointVAD3: The top-level plist property is unset. Setting the AU to bypass mode (no VAD outputs).
[%p] \n Kernel Plist: Fmax %5.3f
%25s:%-5d Possibly no initialization for SubbandDOA(prop id: %d).
[%{public}.*s] BRIR processing failed for source #%u: %d
%25s:%-5d Setting the format defaults.
[%s|%s] SoundStages not initialized
[%s|%s] Biquad dictionary misses one or multiple entries
%25s:%-5d Sample rate for NNNS is not supported! Setting AU in Bypass mode.\n
%25s:%-5d AUBeam2: Error no diffraction filter data
%25s:%-5d CircularModels: Target distance not set to (%f), it remains at the current value (%f). Distance must be nonnegative.\n
%s: Invalid wave file path: %s
%25s:%-5d Input size of SpatialProbabilityInputPostMask is not equal to the expected size (prop id: %u).\n
Reset.
%25s:%-5d CADSPUtility:%s:%d: HOA Error; Incorrect channel count (i.e. not consistent with HOA order definition Channels = (order+1)^2)
[%p] NeuralNet output size (%zu) not matching configured number of output channels (%u) times number of outputs per block (%u).
%25s:%-5d preflight failed
%s:%i will try to construct
%s:%i blending graph is null
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve NumLayers.\"
%25s:%-5d Getting property CurrentBeamCoeffs failed (prop id: %d).
%25s:%-5d allocated %zu bytes of tensor data
%25s:%-5d Shape parameter not set to (%f), it remains at the current value (%f). Valid range is >= 0.\n
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"InputChannelLayouts\"] has invalid value
[%s|%s] Inconsistent data for parameter = %u, element = %u
[%s|setProperty] (scope=%u, element=%u): spatial mixer property dictionary: invalid size %u, expected %u
%25s:%-5d Number of microphones in the plist (%d) does not match the actual number of microphones (%d). Setting the AU in bypass mode.
%25s:%-5d IgnoreTelemetry property length (%lu) doesn't match channel count (%u). Ignoring telemetry.
[%s|%s] EABL ingestion: can't process since the ImmersiveRendererData configuration has not been set
%25s:%-5d iPMWF: successful reset.\n
%25s:%-5d ERROR: Input and output formats need to be equivalent, but we have:\n[Input:  %s], and\n[Output: %s]
[%s|%s] Failed to set high crossover HPF coefficients
[%p] NeuralNet input size (%zu) not matching configured number of input channels (%u) times block size (%u) times batch size (%u).
%25s:%-5d SelectBeamsFrom set to a value greater than number of beams. Setting it to mNumBeams-1.\n
compiling \"%s\"
%25s:%-5d Could not fully parse all essential plist params.
[%s|%s] Setting %u exclusion zones on Input Element %u
[%p] Output is not mono
%25s:%-5d System not configured properly for Convoy input stream, clParams=%p, convoyParams=%p, cal=%p, ConvoyCal=%p
%25s:%-5d RenderTime %d, RenderTimeDelta %f, HostTime %f
uplink speech mixer %p failed to process with error %s (status %s)
[%p] Invalid number (%u) of input buses requested. We only support 1 bus.
%s:%i AUDereverb registration failed
[%p] cached embedding has mismatch size: %lu != %lu
[%p] TaskID read from the plist.
Successfully initialized.
[%s|%s] Initialize channel processors called before the input element is initialized
[%{public}.*s] was already initialized with a blocksize of %zu, bank mode %d
[%s|%s] No suitable vDSP DFT size could be found for the provided HRIRs.
[%s] After frequency grouping, there will be %u bands in total
%s:%i loading from %s failed, caught std::system_error %d: %s
%25s:%-5d Loading BlockSize from topLevelDict.
%25s:%-5d AUBeamNF: Error: Initialized
%25s:%-5d Flushing a log.
%25s:%-5d iPMWF: successful clean-up.\n
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing vector Data from dictionary Bias.\"
[%p] Latency for model: %s is %f
Initialize.
%25s:%-5d Could not load NeuralNetVAD plist, exception (%d).\n
%25s:%-5d DirectionalTargetElevation not found, being set to (%g).\n
%25s:%-5d Spatial capture graph source generation: bad number of mics provided: %u
%25s:%-5d inDataSize %d does not match expected size %d
%25s:%-5d AUBeam2::SetBetaVector (%p)
[%s|%s] Failed Spatializer initialization (%d)
%25s:%-5d Failed to get Version key.
%25s:%-5d NeuralNetRES: Loading FFT2Mel matrix from topLevelDict.
%s:%i initialize processing graphs
%u|%u
%25s:%-5d Loading plist file for %s from %s
%25s:%-5d EXCEPTION (%d) [numStates_ref.get_cf() == nullptr is false]: \"Failed to retrieve NumStates from InputOutputStates.\"
%25s:%-5d Use DYNAMIC batch size (batch size = %d)
%25s:%-5d Override SpCl Property with defaults clsp_srdc %f
AGC VAD received %u input frames with maximum block size of %u frames
%s %s: aufx %s appl created; using BaseProcess
%25s:%-5d Preparing MIL2BNNS NeuralNet implementation.
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Size from dictionary InputVectorDescriptor.\"
%25s:%-5d ECleeSignals cannot be NULL. It is a required input\n
%25s:%-5d AUBeamItTD: in BeamformerTD::MakePHATBeam. Not sure what to do here. For now just run the same thing as SRP mode.
%25s:%-5d AUBeamItTD: in BeamformerTD::MakeLSDDBeam. Not sure what to do here. For now just run the same thing as SRP mode.
%25s:%-5d Restoring plist from AU preset
[%p] Tried to select a VP mask indexed at (%u), but only (%u) masks are available
[%s|%s] PPV2 is being initialized...
%25s:%-5d AUBeam2: Error: Failed initializing Beam2N object
%25s:%-5d CADSPUtility:%s:%d: HOA Error; Empty azimuth/elevation
%25s:%-5d Could not create staged kernel!\n
Trying to set embedding vector, but embedding buffer is not available.
%25s:%-5d Logging level set to: %d
%25s:%-5d AUSpeakerProtectionV3::SetProperty - VP Mode %s->%s\n
%s:%i BypassEffectWithLatency state changed to: %d
%s:%i Transition Wait Time (frames) set to: %u
[%s|%s] (scope=%u, element=%u): invalid property ID %u
[%s|%s] Replacing custom XTC IR using CFURL %@
%25s:%-5d Successfully retrieved DirectionalTargetAzimuth (%g).\n
Running Destructor...
[%s|%s] No center frequencies fell in the %s shelving band; leaving gain at 0 dB.
[%{public}.*s] late processor failed with error %d
%25s:%-5d NeuralNetRES: Loading SampleRate from topLevelDict.
[%s|%s] Solo: could not set input #%u to %s, err = %d
[%p] failed to initialize - I/O sample rates must be equal
[%p] cannot process %u output channel streams (expected channel stream count is %u)
%s:%-5d Number of Input Elements provided is greather than the Maximum supported.
[%s|%s] Error %d setting HeadLocked on group id = %u to %s
Register VolumeTaper
%u frames, %u bytes/frame, expected %u-byte buffer; ioData.mBuffers[%u].mDataByteSize=%u; kAudio_ParamError
%25s:%-5d MultiRadixFFT_Create() returned an error attempting to create mCplxFFTSetup_Cepstrum. Invalid block size?
[%s|setPropertyDictionary] (scope=%u, element=%u): 
%25s:%-5d AUDereverb: Successfully initialized.\n
[%s|%s] ERROR: could not compute the panning gains, err=%d
%25s:%-5d mUsingBlockProcessor: %u\n
Failed to create new music propstrip plist
%25s:%-5d CADSPUtility:%s:%d: VBAP Error; Can not calculate gain for a source location [0, 0, 0]
[%{public}.*s] AULeanSpatial: initialized at %dHz with %d input source(s), bank mode %u, param count = %d
[%p] mNeuralNet input size: %lu
[%s|%s] can't find dynamics processor %s (%u).
%25s:%-5d AUNeuralNetRES: Initialize.\n
%25s:%-5d cached BNNS IR '%s' open failed (%s) -- leaving entry in place
%25s:%-5d Enable CL -> CLThermalEnabled, PilotToneEnabled: %s
%s:%-5d destroyed
[%s|%s] ParseRendererData: Input Element #%u for ASC #%u does not exist
[%p] Could not create NeuralNet model using the plist, exception (%d)
%25s:%-5d Loading StreamingMode.
Exception caught in CFURLPropertyCStringInterface::%s
%25s:%-5d RefMicIndex set to a value greater than number of input mics. Setting it to mNumMics-1.\n
NeuralNetImplLoadFromCache: cached batch size (%u) does not match requested batch size (%u) -- discarding stale entry.
VAD autocorrelation length %f ms is larger than %f
%25s:%-5d kAUEndpointVAD3Property_RecurrentVADNonspeechDetectionEvent cannot be directly accessed.
[%s|%s] Failed to set low pass filter coefficients
[%p] failed to initialize - parameter mix frequency must be positive
[%s|%s] Current output audio channel layout is %s
%25s:%-5d AUBeamNF: Error: Number of unique bands is zero, won't dump diffraction filter
%25s:%-5d NeuralNetVAD: Loading VADinAudioOutputMode from topLevelDict.
%s:%i mFOVWasSetLast = %i
%25s:%-5d Ch %d, ConvoyAdaptiveDisplacement requested but configuration missing, defaulting to Open Loop
%25s:%-5d AUBeamIt: Initialize.\n
%25s:%-5d Max state size %u
%25s:%-5d MIL2BNNS Destroying mContext.data
[%s|%s] EABL ingestion: mdFrame: %s
[%p] failed to initialize - cannot operate in variable block size mode
%s:%i failed to load 'AUDereverb' preset
%s:%i failed to set processing graph denoise preset
[%s|%s] error %d setting input scope property %u on %s
%25s:%-5d The FixedArray object cannot be re-allocated to a different length.
%25s:%-5d SelectBeamsFrom set to a value greater than SelectBeamsTo. Setting it to SelectBeamsTo.\n
[%s|%s] ImmersiveRendererData failed to switch to scheduled parameters err = %d
%25s:%-5d Loading sampleRate from topLevelDict.\n
%25s:%-5d Model path not required for MIL2BNNS_PREPROCESSED
[%s] ParametricProcessorV2Wrapper failed to initialise. Running in passthrough mode.
%25s:%-5d Successfully retrieved bias data type (%s) for Layer %zu.
%25s:%-5d AUNeuralNetSPP: Successfully Initialized.\n
[%{public}.*s] source(inactive): setting up BRIR processor
%25s:%-5d AUDereverb: Initialize.\n
Denoise is Disabled - tuning mode reverts to Single Channel
[%s|%s] could not initialize direct reflection IR processor
%25s:%-5d Parameter info for unsupported parameter (%u) requested
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve HangA10.\"
%s:%i param ID %i outValue %f
%25s:%-5d SpCl property size %d less than expected SpCl header size %d
%25s:%-5d FIREngine Exception: %s (Err=%d)\n
%25s:%-5d Successfully retrieved row index data (%lld) at index (%u).\n
[%p] Loading number of output channels from plist.
%s: Filters Updated to IR Data object
%25s:%-5d  Not enough volume map points. Mapping requires 2 or more points. Only found %d.
[%s|%s] ImmersiveRendererData could not set the layout for input #%u, err = %d
%s: error %d setting input stream format %s for %s
%25s:%-5d Unable to create context from precompiled IR -- fallback to MIL compilation
%25s:%-5d Sample rate is not supported! Setting AU in Bypass mode.
[%{public}.*s] number of output channels does not match what was configured during initialization
%25s:%-5d Device supports AU. { screenWidth=%d, screenHeight=%d, screenScale=%f }
%25s:%-5d Successfully set data for property %u (%s)
%25s:%-5d Successfully initialized.\n
[%s|%s] Initializing channel processors
[%p] created captures folder: %s
%25s:%-5d Applying OL displacement params to channel %i:%s
[%s|%s] Failed to extract SoundStage preset: %@
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve sample rate.\"
a single input ABL and a single output ABL is expected, receiver (%u, %u)!
%25s:%-5d Logging DoA to files -- this is not real-time safe! Use only for debugging
[%s|%s] Creating upmixer with FFT size %u
[%s|%s] Invalid audio channel layout: AudioFormatGetProperty returned error %d
[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] (Mic=%u Ref=%u) missing/invalid Coefficients; skipping
%25s:%-5d Write-only property UnlockOrientation was read?
[%p] Invalid number (%u) of output buses requested. We only support 1–2 buses.
%25s:%-5d AUNeuralNetVAD: Start Initialization.\n
%25s:%-5d AUECMicRef: Successfully initialize.\n
%25s:%-5d Successfully parsed all %lu gain-link group params.
%25s:%-5d Failed to load the number of mics from the plist.\n
[%s|%s] Invalid scope %u
[%{public}.*s] source(#%u): setting up HRIR processor
[%{public}.*s] invalid parameters for StateStorageByteSize
set CoreAudio reporter IDs - %s
[Room Congruence] %s: The input exp parameter must be greater than 0 and smaller than 1. Returning empty optional.
%25s:%-5d Found the dictionary InputVectorDescriptor.
%s:%i set CoreAudio reporter IDs - %s
%25s:%-5d AUDenoise: Using logPeriod of (%g)s as specified in defaults write pmwf_log_period_in_seconds.\n
%25s:%-5d EXCEPTION (%d): \"bnnsdict not found in top level dictionary.\"
[%{public}.*s] Late reverb processing failed: %d
%25s:%-5d Could not fully parse the EnableDisplacementControl param. Will use the default.\n
%25s:%-5d Error processing lp noise estimate post-processor, possibly bypassed.
%25s:%-5d Found the dictionary LayerDescriptor.
%25s:%-5d Loading from matrixDict.\n
processing graphs need to be re-created
%s:%i will teardown the internal CAReporterID
%25s:%-5d Successfully retrieved model path (%s).
%25s:%-5d Sample rate is not present in the dictionary.
%25s:%-5d Input size of DenoiseInputMaskEstimate_CF is not equal to the the expected size (prop id: %u).\n
%25s:%-5d Mode=ManagedRingBuffer, Invoking BNNSGraphContextMakeStreaming
[%s|%s] Error creating neural network - inconsistent number of input channels between layout and plist - Layout = %u, Plist = %u
%25s:%-5d AUBeam2 Error: Converting diffraction filter vectors length from tuning file
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Gains\"][%u][\"Gain\"] has invalid value
[%s|%s] Clearing late reverb HOA IR
[%s|%s] IRFileList error or empty list
[%s|%s] Captured preset will be saved to file %@
%25s:%-5d EXCEPTION (%d): \"Unknown Model File name(%s): Only .mil or .ir file extension is accepted\"
%s:%-5d Number of Input Elements provided is less than the Minimum required.
[Room Congruence] %s: Tuning Parameters dictionary invalid - underlying CF object is nil.
[%{public}.*s] inconsistent data size in bank attributes
%25s:%-5d Fixed number of graph input ports different from expected: %u
%s:%i failed to initialize bypass graph - %@
%25s:%-5d Successfully retrieved DirectionalModelShapeParamer (%g).\n
[%s|%s] Scene reverb IR is non-HOA, post-processing reverb will run in parallel.
%25s:%-5d Setting property ConfigPlist
[%{public}.*s] was provided with %zu samples but expected %zu samples to match partition size
%25s:%-5d AUBeam2 Error: Converting eq vectors length from tuning file
%25s:%-5d AUBeam2: Error no post EQ data
[%p] No model found in plist. Cannot set NeuralNetBNNSData_CF before NeuralNetPlist
%25s:%-5d CADSPUtility:%s:%d: HOA Error; VBAP calculation error
%25s:%-5d  Output volume curve cannot be null
[%s|%s] InputProperties for Element#0 in the property dictionary are being selectively applied to all APAC buses.
%25s:%-5d Invalid number (%u) of input buses requested. We only support 1 bus.
%25s:%-5d EXCEPTION (%d) [layer.mWeightsQuantized.size() != weightsNumberOfCoefficients is false]: \"NeuralNetBNNS: Layer (%u), number of weights (%lu) is not matching the required number of weights (%lu).\"
[%s|%s] Created cache with %u entries
%s:%i failed to load 'AUDenoise' preset
%s: reference data file failed to load: %s
%25s:%-5d NeuralNetVAD: Loading DirectionalTargetAzimuth from topLevelDict.
%25s:%-5d Using SpTS calibration: Requested displacement controller for Ch %u was already kOpenLoopDisplacement, as needed.\n
Failed to set AUSpatialMixer output type after not finding factory preset
AudioUnitGetProperty: null size pointer
[%s|%s] Property %u ignored with global sound stage = %u. Post-processing reverb = %u (not changed).
%25s:%-5d Input size of DenoiseInputMaskEstimate is not equal to the the expected size (prop id: %u).\n
%25s:%-5d Successfully retrieved the description (%s) for Beam %d.\n
Register SpatialBalance
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary Bias.\"
AudioUnitSetProperty: inData == NULL
Failed to map 4cc %d to parameter
%25s:%-5d Failed to set graph parameter for output %u in mic selector: %@
%25s:%-5d AUSeparate: Initialize IVA Classes.\n
%s:%i create processing graph (deferred)
%25s:%-5d EXCEPTION (%d): \"failed to open BNNS IR file (%s)\"
%25s:%-5d scope is null
[%s|%s] ERROR: ImmersiveRendererData_V2 struct truncated
[%p] Truncate of freq domain data not allowed (except nyquist)
%25s:%-5d EXCEPTION (%d) [mDNNLayer[layerIdx].mFilter == nullptr is false]: \"NeuralNetBNNS: Layer (%u), filter not created.\"
[%p] AUReferenceSignal's property list \"Configurations\"[%u] has invalid \"Name\" value
[%s|%s] ERROR: cannot process with %d output channels
%25s:%-5d EXCEPTION (%d) [mGraph.data == nullptr is false]: \"unable to compile program %s\"
[%{public}.*s] activated source slot %u with requested ID: %u
[%s|%s] Unknown global param id %u
%25s:%-5d initialized\n
[%{public}.*s] Failed to re-initialize unique late processor with state memory
[%s|%s] invalid scope = %u for property = %u
%25s:%-5d Input size of PriorSPP  (%lu) is not equal to the the expected size  (%lu) (prop id: %u).\n
%25s:%-5d DirectionalTargetAzimuth not found, being set to (%g).\n
%25s:%-5d EXCEPTION (%d): \"Unsupported output data type.\"
[%p] \n Kernel Plist: NumIntevals %u
%25s:%-5d Incorrect number of input samples! Received %d, but expected %d.
Failed to set AUDSPGraph graph test file path, trying legacy location
[%p] Tried to select a model indexed at (%u), but only (%u) models are available. A new model will not be selected and the previous selection will be used.
%25s:%-5d Input size of DenoisePostMaskEstimate_CF is not equal to the the expected size (prop id: %u).\n
%25s:%-5d Successfully loaded NeuralNetNS plist.\n
%25s:%-5d EndpointVADSegmentHeuristics: Input VAD sequence exceeded the internal history size.
%25s:%-5d AUBeamNF Error: Converting diffraction filter vectors length from tuning file
[%{public}.*s] cannot set BankMode to BothEars when initialized with only 1 output channel. Defaulting to LeftEar
%25s:%-5d EXCEPTION (%d): \"Unsupported bias data type.\"
%s: error %d resetting %s
[%p] DSPGraph input bus format: %s don't match expected format: %s
%25s:%-5d AUECSUMO::ProcessMultipleBufferLists error - wrong (%u) block size expected (%u)\n
VolumeTaper registration failed
[%{public}.*s] carved FP16 conversion buffers from external state memory (%zu bytes)
%25s:%-5d Creating graph from model
[%p] Failed to retrieve embedding mode
[%s|%s] Failed to compute the warping result for the given tuning and input RT60 data. Returning empty optional.
[%{public}.*s] failed initialization. The processing delay %zu would be higher than the bank's data offset %zu. Please switch the bank to the hybrid T+D mode
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"InputChannelLayouts\"][%u] has invalid value
[%s|setProperty] (scope=%u, element=%u): %s = %s
%25s:%-5d Could not create kernels, because no plist has been successfully applied. (You must set a plist and re-initialize, or we will apply 20dB of attenuation during processing.)
[%s] SteeringVectorsIRDataPath cannot be changed after calling Initialize().
%25s:%-5d Failed to create graph from model, error: %@
%s:%i failed to set bypass graph delay parameter - %@
[%p] gain vector format not supported
[%s|%s] Incorrect number of channel processors for parametric rendering %u
%25s:%-5d AUECMicRef: AOPMode detected (non-realtime logging).\n
%25s:%-5d AUBeam2::~AUBeam2 (%p)
%25s:%-5d Directory does not exist %s
[%{public}.*s] initializing SRCs
Successfully initialized.\n
[%s|%s] Failed to set low crossover HPF coefficients
%s:%i DereverbEnable set to: %u
[%s|%s] Failed creating HOA decoders
%25s:%-5d NeuralNetVAD: Loading NumLayers from topLevelDict.
[%{public}.*s] cannot pull more samples than partition size (asked %zu, max %zu)
%25s:%-5d  CAMutex::CAMutex: Could not init the mutex
[%s|%s] ERROR: could not export the preset to %@
%25s:%-5d AUECMicRef: Initialize.\n
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve WaitFrames.\"
%25s:%-5d CADSPUtility:%s:%d: VBAP Initialization Error; Empty or inconsistent vertex set
[%s|%s] Constructed
%25s:%-5d AUECSUMO: AOPMode detected (non-realtime logging).\n
[%s|%s] The selected closest preset is not supported. Returning empty vector.
%25s:%-5d Invalid value for combined probability mode (%u).\n
SetProperty(kAudioUnitProperty_DspLibDictionary) Error: unknown plist format\n
AULoudspeakerSystemIDV2::Initialize failed — algorithm is null (gInstanceCounter=%u)
[%p] Could not load metadata using the plist, exception (%s)
[%p] ModelNetPathBase is overriden to %s
[%s|%s] NeuralRAD loaded with %u inputs and %u outputs
%25s:%-5d SpatialProbabilityBase: Shape parameter max not set to (%f), it remains at the current value (%f). KappaMax should be >= (%f).\n
[%p] AU has no input busses
[%s|%s] ERROR, Upmixer did not initialize properly
%25s:%-5d Number of channels key does not match plist number channels
[%s] Synthesis averaging coefficient set to %.3f
%25s:%-5d Successfully retrieved sample rate (%u).
[%p] failed to initialize - I/O channel counts must be equal
[%s|%s] Applied
%25s:%-5d <-%s %p: Swallowed exception from Close()
%25s:%-5d AUECMicRef::ProcessMultipleBufferLists error - wrong (%u) block size expected (%u)\n
%25s:%-5d AUDenoise: Initialize PMWF Classes.\n
[%{public}.*s] setting up late reverb processor (unique instance)
AUDSPGraph registered successfully
%25s:%-5d Successfully loaded DistanceEstimator plist.\n
%25s:%-5d required key missing '%s'
VAD LPC block size is %d
%s:%i check input and output formats
%25s:%-5d Failed to retrieve sample rate.\n
%25s:%-5d Trying to set peakFinderWindowTime_ms past max capacity
%25s:%-5d CADSPUtility:%s:%d: HOA Error; initializing a HOA instance with order = %d > 3 with FuMa normalization
%25s:%-5d <-%s %p
%25s:%-5d Fixed beam selection mode is chosen. Setting SelectBeamsTo = SelectBeamsFrom.\n
[%{public}.*s] Error processing input SRC (%u)
[%{public}.*s] allocated state storage: %zu elements (%zu bytes) for %zu sources
[%s|%s] FFT size set to %u
[%p] NeuralNet initialization using plist in AUNeuralNet failed with an unknown exception.
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Orientations\"][%u] has unsupported value
tuning mode set to %u
[%p] check input format before initialization
[%s|%s] dispatching update for InputElement #%d:
%25s:%-5d AGC failed to process.
%25s:%-5d SetProperty ID=%d scope=%d bus=%d\n
%25s:%-5d NeuralNetVAD: Loading HangA10 from topLevelDict.
Tensor pointers are nullptr in process(), returning empty output
%25s:%-5d Successfully retrieved number of beams (%i).\n
[%s|%s] Could not set the post-processing reverb blend to 50 on group id = %u, err = %d
%25s:%-5d ECoutSignals cannot be NULL. It is a required input\n
%25s:%-5d AUECMicRef: Using logPeriod of (%g)s as specified in defaults write ecmicref_log_period_in_seconds.\n
[%{public}.*s] silent output period begins. Input has been silent for %f s
%25s:%-5d Missing dictionary: %s\n
%25s:%-5d Successfully parsed all the per-speaker OL thermal params.
%s: could not load preset %s
[%s|%s] Biquad Stage %u error -- non-finite parameter; replacing with bypass filter
[%s|%s] ERROR: Azimuth and/or Elevation vectors are empty.  Default to stereo
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"SampleRate not loaded\"
[%s|%s] Initializing ScottyLite
%25s:%-5d Requested ConvoyAdaptiveDisplacement but ParameterUpdaterConfig key is missing from spp3 plist
[%p] TaskID not available in the plist.
[%{public}.*s] AULeanSpatial::AddSourceParameters: added %u new parameters for %u sources
[%p] AUReferenceSignal's property list \"Configurations\"[%u] has invalid value
[%s|%s] Could not load BiNeural
%25s:%-5d Could not fully parse ignore-telemetry information. All speakers will honor telemetry.
%s:%i failed to flush logs due to exception
%s:%i internal CAReporterID is already set to %llu
[%s|%s] error %d setting kAudioUnitProperty_MaximumFramesPerSlice on %s
%25s:%-5d AUBeamNF::SetBetaVector (%p)
%s:%-5d Successfully retrieved Algorithm Core Type MicIssueDetectorCorev1 \n
[%s|%s] Couldn't find user data for the selected IR preset. Returning %s.
parseDictionary() Error: length is %lu, but should be %d
[%{public}.*s] inconsistent delay size in bank attributes
failed to run bypass graph
%s: error %d setting input audio channel layout for %s
%25s:%-5d AUECMIMO: ********* Logging ends *********\n
%25s:%-5d No entry in biquad .plist for sample rate of %.0f!\n
%25s:%-5d Finish reading NeuralNetVAD parameters: SampleRate=(%d)); Threshold=(%4.2f); NumLayers=(%d); WaitFrames=(%d); BlockSize=(%d); Context=(%d); FeatSize=(%d)
%25s:%-5d AUDenoise: ********* Logging ends *********\n
%25s:%-5d EXCEPTION (%d) [!validContext is false]: \"Unable to load BNNS Context\"
%25s:%-5d Read plist key: %s = %f
%25s:%-5d Successfully created graph from model
%25s:%-5d Done initializing result = %i
%s: WARNING: AUXTC file not found at %s
[%s|%s] update dropped
%25s:%-5d AUECMIMO: ********* Logging begins *********\nAUECMIMO: logging (period, timestamp): (%f, %f) (s)\nAUECMIMO: state variables have finite values (1 if True): %u\nAUECMIMO: ref-signal buffers have finite values (1 if True): %u\nAUEC
[%s|%s] The new target mid-band RT60: %f. The new target room volume: %f
%25s:%-5d Loading from inputDescDict.
%25s:%-5d ->%s
%25s:%-5d Embedded VarEQ fails with error %u
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"NumInputChannels not loaded.\"
%25s:%-5d Attempting to set an unsupported property: %u
%25s:%-5d Successfully retrieved InputScale (%g).\n
[%s|%s] Unknown metadata version %u.%u
[%s|%s] Error with output stream format with error code %d
%25s:%-5d NeuralNetVAD: Loading SpatialSPPCutOff from topLevelDict.
%25s:%-5d Input size of DenoisePostMaskEstimate is not equal to the the expected size (prop id: %u).\n
%25s:%-5d Identified %u streaming pairs
[%s|%s] ERROR: ImmersiveRendererData_V1 struct too big
Failed to set Voice dictionary
%25s:%-5d Cannot read plist key: %s
[%s|%s] Scotty Bypass %i
%25s:%-5d Block size is not supported! Setting AU in Bypass mode.\n
%25s:%-5d Initialize Spatial Probability Classes.\n
%25s:%-5d NeuralNetVAD: Loading DeltaFeature from topLevelDict.
[%p] \n Kernel Plist: FullLen %u
[%s|%s] Merging current room preset with input preset.
[%{public}.*s] process error, i/o buffers are null
[Room Congruence] %s: The input k parameter must be greater than 0. Returning empty optional.
[%s|%s] ImmersiveRendererData: all channel info sizes are not equal
%25s:%-5d BeamFarfieldEQ found in plist.
%25s:%-5d Fmax must be < (samplingRate/2). Setting Fmax = samplingRate/2.\n
Failed to open austrip file
[%{public}.*s] TD coefficient size larger than needed (%zu vs %zu) - will use first %zu partitions, ignoring %zu trailing samples
[ECv6] SetProperty(ECIR) rejected: AU already initialized (mic=%u)
%s:%i %s latency %f does not match %s delay latency %f
%25s:%-5d Input size of SpatialProbabilityInputCDR is not equal to the expected size (prop id: %u).\n
[%{public}.*s] source(#%u): setting up BRIR processor
%25s:%-5d Setting property BeamformerCoeffs failed (prop id: %d). *inData should be CFDictionaryRef. Provided inDataSize = %u.\n
%25s:%-5d Applying OL thermal params to channel %i:%s
[%s|%s] Could not acquire the lock. SoundStage warping not done.
[%s|%s] Error creating neural network - NeuralRAD does not support multiple LFEs
%25s:%-5d CADSPUtility:%s:%d: VBAP Error; Unable to change speaker locations, azimuth and elevation have different sizes
%25s:%-5d AUBeamNF: Error: Failed initializing BeamNF object
%25s:%-5d AUECSUMO: ERLE measure in [dB] for mic-channel %u , internal: %f (dB), external: %f (dB)\n
%25s:%-5d Successfully retrieved sample rate (%iHz).\n
[%s|%s] Distance Attenuation: Failed to get the distance params
%25s:%-5d Error initializing ASA features DSP chain: %s
%25s:%-5d Ch %d, SpClProps:\n%s
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary InputVectorDescriptor.\"
%25s:%-5d Missing dictionary %s.\n
[%p] \n Kernel Plist BaseShiftsPerInt : 
[%{public}.*s] AULeanSpatial: constructed
%25s:%-5d Using synchronized worst case displacement controller values w_0=%f, x_ul_norm=%f, Q_d=%f, G_bw=%f
%25s:%-5d Could not fully parse the power smoothing time constants. Will use the default
[%s|%s] ERROR, not intialized
[%s|%s] Resetting Crossover2f
[%s|%s] Resetting HRTFHQ reverb
%25s:%-5d Loaded implementation from cache for model at %s.
[%s|%s] EABL ingestion: mdEvent: eventType = %u, channelIndex = %u, eventSize = %u, eventStartTime = %f, audioFrameCount = %u, version = %u
[%{public}.*s] TD coefficient size (%zu) not evenly divisible by numChannels (%zu)
[%{public}.*s] LSBank: start of fadeout is beyond end of filter
%25s:%-5d AUBeam2: Error: Could not open post EQ file %s
[%s|%s] Could not load NeuralRAD
%25s:%-5d CLSPKernel_v5::CalcCoeffsSyncDisp
[%s|%s] Could not reset directivity index on sc #%u, input element #%u
%s:%i internal CAReporterID destroyed
%25s:%-5d Successfully parsed the %s plist entry for channel %i.
%s:%-5d created
%25s:%-5d CADSPUtility:%s:%d: VBAP Error; Can not calculate gain if the VBAP object is not initialized
%25s:%-5d error in graph process
%s:%i failed to set processing graph dereverb preset property
[%s|%s] Output layout tag %s is not supported for Diffuse
%25s:%-5d Delay %f ms at fs=%f is bigger than delay buffer of %u samples
%25s:%-5d Unlock requested while already unlocked?!
[%s|%s] Trying to render while initialization or clean-up is in process
%25s:%-5d Saved implementation to cache for model %s (batch size %u).
[%{public}.*s] LSSource::initialize: insufficient state storage: got %zu elements, need %zu elements
[%s|%s] Could not initialize channel processors after number of channels in a stream changed to %u: error = %d
[%s|%s] AUSM_HRIR: Personalized HRIR type %u is loaded.
%25s:%-5d DeltaFeature not found, being set to (%u).\n
%25s:%-5d NeuralNetVAD: Loading Directional Model Shape Parameter from topLevelDict.
%25s:%-5d EXCEPTION (%d) [modelNetExt == \".ir\" is false]: \"No MIL fallback option available\"
%25s:%-5d AULoudnessWarrior construction starting\n
[%s|%s] Created caches with %u entries:%s%s%s
%s| Non-existent SharedIRBus channel
[%s|%s] ImmersiveRendererData: dump %s
Init: Failed to set AUDSPGraph input stream format
Failed to get AUSpatialMixer factory presets
%25s:%-5d Reseting the distance estimator.\n
%25s:%-5d Successfully retrieved weights data type (%s) for Layer %zu.
[%p] set 'mModelNetBNNSData'
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"OutputChannelLayouts\"][%u] has insufficient byte size
%25s:%-5d Loading FFT2Mel matrix from topLevelDict
%25s:%-5d parameters changed after Initialize, which will allocate memory on the realtime audio thread - only SetParameter before Initialize\n
bypass preflight gave invalid number of frames to process!
[%{public}.*s] process error, output channel #%u is null
%25s:%-5d Successfully parsed the EnableCPMSControl param: [ %s ]
[Room Congruence] %s: The input RT60 to be warped must be greater than 0. Returning empty optional.
[%s|%s] Distance Attenuation: Failed to set the distance params
Failed to create new music austrip plist
[%s|%s] invalid input channel layout %d
%25s:%-5d Invalid treble EQ sizes: BQ vector has %lu coefficients\n
%25s:%-5d SpCl version not recognized in SpCl header: 0x%x
%25s:%-5d AUJBase init failed: %d\n
%25s:%-5d AUBeam2: Error: Could not open diffraction filter file %s
%25s:%-5d Construct NeuralNetEspresso.
%25s:%-5d Found the dictionary: %s\n
parameter %d is missing
%25s:%-5d Initializing with Smoother release TC: %s
[%s] Reusing cached SHbasis, HRTFs, Mdec, and gridWeights
Setting orientation %u on %s
%25s:%-5d kAUEndpointVAD3Property_EndpointerSpeechDetectionEvent cannot be directly accessed.
[%s|%s] Invalid number of input channels %u
%25s:%-5d Successfully parsed all %lu speaker name params.
kAudioUnitErr_TooManyFramesToProcess : inFramesToProcess=%u, mMaxFramesPerSlice=%u
[%p] \n Kernel Plist: Len %u
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Gains\"][%u] has no \"Output\" key
[%p] Defaulting to NeuralNet model (%u) for processing.
[%s|setPropertyDictionary] (scope=%u, element=%u): unsupported data type for dictionary entry %u
%25s:%-5d kAUEndpointVAD2Property_EndpointerNonspeechDetectionEvent cannot be directly accessed.
[%s|%s] Number of channels in AudioChannelLayout = %u does not match number of channels in stream format = %u. Reverting to default layout.
throwing %d
%25s:%-5d  key 'DSPchain' not found
%25s:%-5d Loaded output channel layout %s (%u) from tuning plist 
successfully retrieved spectral profile sample rate with ambiguous conversion (%u Hz)
[%{public}.*s] RightEar mode requires 2 coefficient channels, got %zu
[%{public}.*s] transform scratch too small (need %zu floats, got %zu)
%25s:%-5d Zoom curve loaded from %s
[%s|%s] Setting default audio channel layout tag = %s for %u channels
%s:%i failed to reset processing graph - %@
%25s:%-5d Clearing the value of property %u (%s)
%25s:%-5d AUBeamNF: Error: Number of unique bands is zero, won't dump post EQ
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve InputScale.\"
Failed to set AUSpatialMixer output stream format
%s:%i create processing graph
%s: Filters can not be generated if the number of drivers is < 2
[%s|%s] [OutputElement] Error setting audio channel layout: null layout pointer
Trying to set embedding value, graph tensor unavailable or size mismatch.
Failed to set uninitialize AUDSPGraph graph
%25s:%-5d iPMWF: successful initialization.\n
[%p] input format: %s
%25s:%-5d  could not load DSPchain
[%s|%s] EABL ingestion: Mismatch between the configured number of channels and the actual number of channels of the first input
SetProperty( kAudioUnitProperty_DspLibDictionary ) Error : importer : %s\n
[%s|%s] Biquads not updated - lock not acquired
%25s:%-5d No tuning dictionary
[%s|%s] mTuningMatrix should be an identity matrix by default
%25s:%-5d Missing dictionary RealCoefficients.\n
%25s:%-5d  CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)
[%p] NeuralNet expects input block size %u, and we received %s.
[%p] \n Kernel Plist Levels Per Interval : 
%s %s: could not find aufx %s appl
%25s:%-5d Retrieved (unset) property data for property %u (%s)
MeisterStueck registration failed
[%s|%s] Sufficient filter parameter changes occurred --- recalculate filters
%25s:%-5d %s\n
%25s:%-5d Using SpTS calibration: Requested displacement controller type (%u) for Ch %u is overridden to kOpenLoopDisplacement.\n
%25s:%-5d AUDistance: (MCLPOutSignals, ECOutSignals) is NOT finite: (%d, %d)
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary InputVectorDescriptor.\"
[%p] \n Kernel Plist: Fshift %5.3f
[%p] AUReferenceSignal's property list \"Configurations\"[%u] has no \"Orientations\" key
%25s:%-5d Successfully retrieved number of context frames (%u).
%25s:%-5d Cannot get value of NumChannels from the plist.
[%s|%s] Could not set reverb preset for sc #%u, input element #%u, err = %d
%25s:%-5d AUNeuralNetSPP: Initialize.\n
[%s|%s] invalid parameter id %d (global scope)
[%{public}.*s] source(#%u) was already initialized with different settings, will reinitialize processors
[%s|%s] Failed to initialize MagLS cache.
[%s|%s] Failed to initialize SoundStage.
%25s:%-5d Successfully retrieved MCLPOutScale (%g).
%25s:%-5d NeuralNetVAD: Loading NumContextFrames from topLevelDict.
[%s|%s] Reflattening Biquads: Biquad A: freq = %f [Hz], gain = %f [dB], Biquad B: freq = %f, gain = %f.
%25s:%-5d Orientation %u is smaller than the minimum allowed value (%u)
%25s:%-5d Override SpCl Property with defaults clsp_caltemp_r %f
[%s|%s] ImmersiveRendererData does not support render type %u. Fallback to object.
  from %s, process err: %d
[%s|%s] GetParameter failed, err = %d
[%s|%s] eventOffsetInAudioBuffer (%d) = mCurrentMDHeader->frameStartTime (%d) + mCurrentMDEvent->eventStartTime (%d) - mFirstAudioBufferSampleTime (%d)
[%s|%s] Error creating Low Frequency ALLRAD Decoder
%s:%i unsupported order!
%25s:%-5d UseDirectionalMode not found, being set to (%g).\n
%25s:%-5d ERROR: Input bus (%u-ch) and output bus (%u-ch) have different channel counts.
[%p] Successfully retrieved embedding mode (%g).
[%s|%s] ERROR: wrong number of output channels %d
[%s|%s] Unknown output type %d
[%s|%s] Could not set the post-processing reverb blend to 0 on input %u, err = %d
%25s:%-5d Initialize called without setting the layers plist! Setting AU in Bypass mode.
[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] missing Mic/Ref; skipping
%25s:%-5d AUECSUMO: energy measure in [dB] for ref-channel %u : %f\n
%25s:%-5d Could not fully parse the power smoothing time scales. Will use the default
[%s|%s] Error creating neural network - %u output channels is not supported
Setting bypass to %u
%25s:%-5d AudioUnitGetProperty failed for %s
%s:%i NeuralNetPresetPathOverride is set to null and thus removed
%25s:%-5d Binding buffer for input state %s
[%{public}.*s] invalid frame count for source %u, got %u, expected %zu at max
[%s|%s] Error %d setting StereoPanningRefAngle on group id = %u to %f
[%s|%s] Neural Spatializer Constructed
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Gains\"][%u] has no \"Gain\" key
%s:%i InitializeProcessingGraphs failed
%s:%i failed to set blending graph delay parameter
%25s:%-5d AUNeuralNetVAD: Successfully Initialized.\n
%25s:%-5d AUBeamNF::DumpDiffractionFilter (%p)
[%s|%s] Global property %@ in the property dictionary is applied separately.
[%s|%s] ImmersiveRendererData failed: inconsistent rendererDescription channel boundaries for rendererDescription #%u: %u, %u
[%s|%s] ERROR: Could not capture preset
%25s:%-5d Reset.\n
[%p] failed to locate propstrip file - %s
[%s|%s] ImmersiveRendererData:  kImmersiveRendererType_Unspecified used for input #%u. Fallback to object.
[%s|%s] Error: not enough renderer data elements
[%s|%s] No default for enum value %u. Building on top of Neutral instead
bypass graph not initialized
[%s|%s] updating late reverb
[%s|%s] [OutputElement] Invalid element %u
%25s:%-5d Check output form\n
%25s:%-5d NeuralNetVAD: Loading forgetting factor Lambda_TC from topLevelDict.
Failed to set new music AUDSPGraph graph text file path
[%s] Grid weights were not found in .ir file. Computing on the fly, which will likely be very slow...
[%s|%s] Unsupported input channel count %u
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"OutputChannelLayouts\"][%u] has unexpected byte size
%25s:%-5d MultiRadixFFT_Create() returned an error attempting to create mCplxFFTSetup. Invalid block size?
%25s:%-5d NeuralNetEspresso constructed.
%25s:%-5d AUSpeakerProtectionV3::SetProperty - IgnoreTelemetry. Could not be fully parsed (invalid data?).\n
[%s|%s] Could not set reverb preset for group id = #%u, err = %d
[%s|%s] Neural Transcoder Successfully Initialized
%u frames, %u bytes/frame, expected %u-byte buffer; ioOutputBufferLists[%u]->mBuffers[%u].mDataByteSize=%u; kAudio_ParamError
[%p] cannot process %u input busses (expected input bus count is %u)
%25s:%-5d AUEchoGateV3: Gate [%s], Cutoff = %f, Transition band = %f @ %fdB/%fHz
%25s:%-5d Successfully retrieved UseDirectionalMode (%g sec.).\n
%25s:%-5d MIL2BNNS: Unexpected exception in destructor!
[%{public}.*s] deactivating source #%u
AUECRMDF::Init warning - tried to set mOrder: (%u), but forced mOrder to (%u)\n
%25s:%-5d CADSPUtility:%s:%d: subtriangle still not found in computing rank with relaxed test!
%25s:%-5d Failed to set reference mic index: %@
[%p] NeuralNet0 lookaheadSize (%u) and NeuralNet%u lookaheadSize (%u) do not match
[%{public}.*s] constructed (%lu-bit)
[%s|%s] ImmersiveRendererData failed to set the number of input elements for input #%u, err = %d
[%s|%s] ImmersiveRendererData: Could not configure %u (%s) renderer type (1), input #%u, err = %d
[%p] Initialize finished with error code %u \n
[%s|%s] ERROR: Could not create mixer output capture file (ExtAudioFileCreateWithURL returned %d)
%25s:%-5d Failed to set up internal audio units.
%25s:%-5d EXCEPTION (%d) [modelPlistInfo.streamingMode_int >= static_cast<UInt32>(StreamingMode::NumModes) is false]: \"StreamingMode (%u) is out of range, a value smaller than (%d) is expected.\"
%25s:%-5d Sample rate is not supported! Setting AU in Bypass mode.\n
[%s|%s] Spectral matching gains [dB]: LG: %f, MG: %f, HG: %f.
[%s|%s] Cleanup was not done appropriately (2)
[ECv6] LoadPendingIRsFromDictionary: header exceeds bounds (NumMics=%u NumRefs=%u FilterSize=%u; max mics=%u, max refs=%u, max filterSize=%u)
%25s:%-5d Successfully retrieved NumContextFrames (%u).\n
[%s|%s] Setting stream format: %s
%25s:%-5d AUBeamNF Error: Converting eq vectors length from tuning file
%25s:%-5d AUECMicRef: Cleanup.\n
%25s:%-5d kAUEndpointVAD2Property_DoneProcessingAudioForNonRealTimeDecode is write-only.
%25s:%-5d inDataSize %d < expected size %d
%25s:%-5d Successfully parsed the smoothing strategy: [ %s ]
%25s:%-5d Could not fully parse the power smoothing strategy. Will use the default
[%s|%s] Setting input channel layout tag = %u (%s)
%25s:%-5d AUDereverb: Cleanup.\n
%25s:%-5d AUECSUMO: Initialize.\n
Output bus must be mono\n
Failed to set configure AUDSPGraph graph for new music
[%s|%s] invalid scope %u
%25s:%-5d Could not load DistanceEstimator plist, exception (%d).\n
%25s:%-5d Initializing with Smoother attack TC: %s
%25s:%-5d Loading WaitFrames from topLevelDict
%25s:%-5d ModelNetPathBase is provided - retriving base path and relative path of the model.
%25s:%-5d Bad object for key '%s'
%25s:%-5d mSampleRate: %f\n
[%{public}.*s] late reverb requires full partition size (%zu), got %u
[%s|%s] ImmersiveRendererData_V1 ingestion has ended
%25s:%-5d EXCEPTION (%d) [weightsDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Weights.\"
%25s:%-5d \tAUBeam2: input stream format: %s
%25s:%-5d AUBeamNF::Cleanup (%p)
%25s:%-5d Successfully retrieved mHangA01 (%g).\n
%25s:%-5d Successfully retrieved HangA10 (%g).\n
%25s:%-5d Could not read CLParams for ch %zul
AUNeuralNet registered successfully
%25s:%-5d In VAD3Configuration::Initialize, Forcing reinitialization of VAD3Configuration.
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing vector Data from dictionary Weights.\"
%25s:%-5d EXCEPTION (%d) [weightsDataType_ref.get_cf() == nullptr is false]: \"Missing DataType from dictionary Weights.\"
%25s:%-5d bnnsdict found in top level dictionary, data loaded.
Warning: %s SetParameter for undefined param ID %u while initialized. Ignoring.
%25s:%-5d scope %u element %u: incoming (invalid) format %s. required fmt %s
%25s:%-5d Orientation locked without waiting for IO thread
[%p] Successfully retrieved lookahead size (%u).
[%s|%s] Standard bypass matrix not available; reverting to a diagonal matrix
failed to migrate AudioUnit assets at \"%s\" path due to uncaught exception
Failed to set ambience TM dictionary property
%25s:%-5d  CAMutex::Unlock: Could not unlock the mutex
%25s:%-5d CADSPUtility:%s:%d: VBAP Error; Duplicate vertices were found
%s:%i DenoisePresetPathOverride is set to null and thus removed
[%s|%s] ERROR: writing data to output file, %d
[%p] AU can only support two output buses but receives %d
%25s:%-5d Found the dictionary (%s).
[%s|%s] error %d initalizing %s; processing disabled
%25s:%-5d graph has %zu arguments
[%s|%s] Uninitializing ScottyUpmixer
[%s] Failed to lock memory
%25s:%-5d This device uses SpTS for speaker calibration, and it has not been applied yet. Will attempt to fetch it.\n
Failed to create AUSpatialMixer instance
AGC VAD SRC failed to process with status %u
%s:%i illegal dominance parameter value: %f
%25s:%-5d NumDictColumns does not match NumColumns we use.\n
%s:%i failed to reset bypass graph - %@
%25s:%-5d \tAUBeamNF: output stream 0 format: %s
%25s:%-5d AUBeamNF: Error: Could not read post EQ file %s
%25s:%-5d Cannot get CLParams Key
[%s|%s] Unknown HRTF type %u
[%s|%s] Could not set exclusion zone array on group %u, err = %d
Failed to set Music EQ Bypass dictionary
[%p] created
%s: error %d initalizing %s; processing disabled
[%s|%s] BiNeural network being loaded...
%25s:%-5d Successfully retrieved input state name (%s).
%25s:%-5d -
%25s:%-5d Found the dictionary %s.\n
%25s:%-5d CircularModels: TargetSV not set. Input length (%lu) and internal length (%lu) do not match.\n
[%{public}.*s] AULeanSpatial: creating source id=%u
%s:%i create bypass graph (deferred)
[%s|%s] Setting reverb send decorr filter coeffs on Channel %u to %u:
[%s|%s] FactoryPreset %u of subtype = %u is already loaded.
[%s|%s] Error scheduling unsupported parameter (ramped with start value unknown) #%u: param = %u, scope = %u, element = %u
%25s:%-5d Input size of SpatialProbabilityInputSourceProbability is not equal to the expected size (prop id: %u).\n
[%s|%s] One or both of the input RT60 was not greater than zero. Returning empty optional.
[%p] output format: %s
[%s|%s] Could not initialize PPV2
%25s:%-5d \tAUBeamNF: output stream 1 format: %s
%25s:%-5d Applying CL params to channel %i:%s
[%s|%s] Could not clear binaural compatibility mode on sc #%u, input element #%u
%25s:%-5d successful clean-up.\n
NonMediaChatRequestedDuckingLevel: invalid propery size
%25s:%-5d Failed to set reported latency, setPropertyError = %@
%s:%i failed to set processing graph %s base path override - %@
[%s|%s] Early reflections IR is HOA: updating late reverb to use same IR file
%25s:%-5d Possibly no initialization for Subband DOA (prop id: %d).
%25s:%-5d Viterbi ring buffer size (in seconds) not found in plist. Resorting to using legacy default value.
[%s|%s] Error creating neural network - error creating plist object
%25s:%-5d _vp: vptimefreqconverter::analyze: not configured for analysis
[%p] AU block size %u
%25s:%-5d Initialize called without setting setting NeuralNetVADLayers plist! Setting AU in Bypass mode.\n
%25s:%-5d AUDereverb: (OutputSignals, MCLPLeeOut) is NOT finite: (%u, %u)\n
%s:%i Setting FOV %f on mDominanceZoom
[%s|%s] Inconsistent member count in ASC ID list
%25s:%-5d Latency will be reported as %fs
[%s|%s] Failed to set high crossover LPF coefficients
%25s:%-5d SpatialSPPCutOff not found, being set to (%g).\n
[%s|%s] Failed to compute the average RT60 for the preset User Data. Returning empty optional.
%s:%i DenoisePresetPath is overridden with an empty string.
failed to calculate expected bypass graph output frame count
[%s|%s] Destructed
%25s:%-5d AUCircArray: (OutputSignals) is NOT finite
Failed to initialize AUDSPGraph
%25s:%-5d Unspecified error in SetSNREstimator().\n
%25s:%-5d Format not supported, input bus %u (format is: %s)\n
%25s:%-5d EXCEPTION (%d) [pNeuralNetImpl == nullptr is false]: \"NeuralNet implementation not initialized.\"
%25s:%-5d FcLimitWindBoost must be < (samplingRate/2). Setting FcLimitWindBoost = samplingRate/2.\n
[%s|%s] Updated %s reverb windows from FDN mixing time: %u samples (xfade: %u)
%25s:%-5d Missing vector ColumnIndices.\n
%25s:%-5d Issue during initialization, discarding graph
[%p] Assuming 1 un-named model exists in the plist
%25s:%-5d Could not fully parse speaker name information. Speakers will use their default names.
%25s:%-5d Could not fully parse the power group descriptions. Will use the default
%25s:%-5d AUBeam2: Error: Initialized
[%s|%s] Can not set FFT size when AU is initialized
[%p] Successfully retrieved lookahead size %u.
%25s:%-5d The number of channels in the output format (%u) not equal to 1.\n
%25s:%-5d kAUEndpointVAD2Property_RecurrentVADNonspeechDetectionEvent cannot be directly accessed.
[%s|%s] Initializing ScottyUpmixer
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"InputChannelLayouts\"][%u] has unexpected byte size
[%p] output GainVector format has %d channels, which is more than the max number of (%d)
[%s|%s] failed to fully parse zone data
%25s:%-5d  Invalid value for kAUSPLMeterProperty_VolumeMap
%25s:%-5d Input size of SpatialProbabilityInputSteeringVector_CF is not equal to the expected size (prop id: %u).\n
%25s:%-5d AUECMIMO: ********* Reset ends *********\n
%25s:%-5d Initialize called without setting setting BeamFormerCoeffs plist! Setting AU in Bypass mode.\n
%25s:%-5d CircArray Exception: %s (error = %d)\n
[%p] The NeuralNetPlist passed to SetProperty is not CFDictionaryRef type or it's null.
set up logs with time stamp \"%s\"
[%s|%s] Invalid FFT size %u
%25s:%-5d Spatial capture graph source generation: bad number of linear spatial beams provided: %u
[%s|%s] ImmersiveRendererData failed: missing renderer descriptions
[%s|%s] Invalid PP reverb
Failed to initialize AUSpatialMixer
%25s:%-5d Cleanup.
%25s:%-5d Target distance not set to (%f), it remains at the current value (%f). Distance must be nonnegative.\n
[%p] failed to initialize - channel map size is not equal to number of output channels
[%{public}.*s] using caller-provided init scratch for TD->FD transform (%zu bytes)
[%s|%s] Error creating neural network - Frame size = %u, Num Inputs = %u, Num Outputs = %u
%25s:%-5d AUSeparate: (InputSignals) is NOT finite: (%u)\n
non-media-chat requested ducking level set to %u
Failed to get Preference: '%s %s'. It exists, but is it the right type?
AU has been bypassed because of low IOCycle duration requirements. Re-initialize the AU to unbypass.
[%s|setProperty] (scope=%u, element=%u): %s: file not found
failed to set up logs due to exception
%25s:%-5d Successfully retrieved beam azimuth (%0.2f).\n
Initialize.\n
%25s:%-5d Successfully retrieved weights data (%g) at index (%zu).
%25s:%-5d AUBeamNF Error: Invalid mic spacing %d
[%p] failed to apply %s at %s - unknown exception thrown
%25s:%-5d NeuralNetVAD: Loading InputScale from topLevelDict.
%25s:%-5d AUEndpointVAD2: The top-level plist property is unset. Setting the AU to bypass mode (no VAD outputs).
uplink speech mixer failed to apply \"%@\" - %@
Failed to initialize new music AUDSPGraph
[%{public}.*s] will truncate %zu excess samples
SetProperty(kAudioUnitProperty_DspLibDictionary) Error : data\n
%25s:%-5d Failed to create matrix
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Gains\"][%u] has invalid value
[%s|%s] AUSM_PRESENTATION_POS: X (left-right): %.4f, Y (back-front): %.4f, Z (down-up): %.4f
[%s|%s] Failed to prepare a writable capture directory.
%25s:%-5d EXCEPTION (%d) [modelNetPathRelative_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPath.\"
%25s:%-5d MIL2BNNS Destructor Completed.
[%s|%s] Inconsistent sizes in RendererMetadata
[%p] destroyed
[%s|%s] Property update dropped
%25s:%-5d mImplType set to value (%u).
%25s:%-5d AUECSUMO: Cleanup.\n
%25s:%-5d Applying system params:%s
[%s|%s] Could not disable exclusion zone for group %u, err = %d
[%p] AUReferenceSignal's property list has invalid \"Configurations\" value
%s: reference data file not reachable: %s
%25s:%-5d EXCEPTION (%d) [modelNetPath_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPath.\"
%25s:%-5d Created CircArray Kernel with %u ins, %u outs, SR: %0.0f, %u order algorithm, %lu beam patterns %u frameSize\n
[%{public}.*s] source created (inactive)
%25s:%-5d Identified Embedding Tensor: %s
[%s|%s] Failed to compute the average RT60 for the target data. Returning empty optional.
[%s|%s] HOA channels: direct %u, reverb %u; Grid points: direct %u, reverb %u
[%p] AcousticPasscodeDec_setProperty called with result %d
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"KalmanProcessStd not loaded.\"
[%s|%s] ERROR: ImmersiveRendererData struct size too small
[%s|%s] %s
[%s|%s] Could not %s post-processing reverb, err = %d
Failed to open new music propstrip file
[%s|%s] Current audio channel layout is %s
%25s:%-5d Latency is %f
%25s:%-5d EXCEPTION (%d) [(mInputSize != mNumMelBands*mNumContextFrames*(1+mDeltaFeature)) is false]: \"mInputSize is wrong.\"
%25s:%-5d Successfully retrieved EQ filter length (%i).\n
%25s:%-5d Failed to retrieve beam azimuth.\n
%25s:%-5d Creating audio logs failed: %s
%25s:%-5d Closed loop checks failed: mCLParams.size=%d, nKern=%d, SpClProps.size=%d
%25s:%-5d Call to MGCopyAnswer() failed.
[%s|%s] Can't set APAC parameter: ASC #%u referenced for group #%u but no input element exists for it
[%p] Received invalid block processor type value %u
[%s|%s] Dispatch queue cleared
[%s|%s] dispatched update for dynamic XTC filter generation:
%25s:%-5d NeuralNetEspressoV2 constructed.
%25s:%-5d BNNSGraphCompileFromFile failed with unknown exception.
%s:%-5d Session ID set by user : %llu
Unexpected number of metadata parameters %zu
%25s:%-5d Constructed.
[%s|%s] Error setting upmixer output layout with error code %d
%25s:%-5d Getting property EnableSubbandDOACalculation failed (prop id: %d).
Register MeisterStueck
%25s:%-5d Unspecified error in SetNoiseEstimator().\n
[%p] Model with TaskID (%s) will be called
[%s|%s] Global property %@ in the property dictionary is a reserved APAC property, hence ignored.
[%s|%s] No center frequencies within the provided range were found. Returning empty optional.
[%{public}.*s] too many frames requested (%u > %zu)
Failed to set Music dictionary
[%{public}.*s] insufficient state memory: got %zu bytes, need %zu bytes
%25s:%-5d CADSPUtility:%s:%d: VBAP Error; VBAP object not initialized
%s:%i failed to reset blending graph - %@
[%s|setProperty] (scope=%u, element=%u): %s not writable
%25s:%-5d AUBeamItFD: (BFMicOut, BFLeeOut, AllUplinkBeams, AllSelectionBeams) is NOT finite: (%u, %u, %u, %u)
%25s:%-5d Compute engine name (%s) not understood. Defaulting to CPU.
%25s:%-5d kAUEndpointVAD2Property_RecurrentVADSpeechDetectionEvent cannot be directly accessed.
[%p] Low Delay block processor not supported for process block size (%d) > NN block size (%d)
%25s:%-5d Failed to read ULDAT highpass filter cutoff frequency from plist.
[%s|%s] Error in initialization
%25s:%-5d Failed to retrieve number of mics used.\n
%25s:%-5d Last orientation / camera direction update mach absolute time was %llu
[%s|%s] Initializing with max frames per slice = %u
[%s|getProperty] (scope=%u, element=%u): %s internal error: getter not implemented
Sample rate mismatch (mic = %u, ref = %u, eclee = %u, out = %u)
failed to compile \"%s\"
[%{public}.*s] initialize error: insufficient external state storage (provided %zu, required %zu)
%25s:%-5d EXCEPTION (%d): \"Unsupported weights data quantization type for Quantization (%u).\"
%25s:%-5d Successfully retrieved column index data (%lld) at index (%u).\n
%25s:%-5d The CFDictionaryRef passed to SetProperty is null.
[%s|%s] Unknown event type: %u
%25s:%-5d AUNeuralNetRES: (InputSignals, EchoEstimates) is NOT finite: (%u, %u)\n
%25s:%-5d NeuralNetVAD: Loading SampleRate from topLevelDict.
[%{public}.*s] cannot create source - engine not initialized
%25s:%-5d SPP plist version %d is not supported.
[%s|%s] Input Element #%u referenced for sceneComponentID #%u does not exist
%s:%i registration successful
[%s|%s] Setting reverb send decorr filter lengths on Channel %u to %u:
[%s|%s] Disposing output capture file
[%{public}.*s] input buffer overflow for source #%u: pushed %u frames but only %zu available (call pullProcessedData before pushing more data)
Registering UI orientation observer %s
AudioUnitGetProperty: *ioDataSize == 0 on entry
processing graphs already created and tuning mode/Sound to Isolate mode changed from %u/%u to %u/%u 
%s:%i set processing graph %s base path override to \"%@\"
%s:%i loading from %s failed, caught std::exception: %s
[%s|%s] Could not enable scene reverb for group id = %u, err = %d
%25s:%-5d %s UsesFaceUpOrientation (%u): %f
%25s:%-5d AUDenoise: Successfully initialized.\n
[%s|%s] Error %d setting Internalized on group id = %u to %s
Failed to set propstrip on AUDSPGraph
%25s:%-5d Failed to retrieve %s.\n
%25s:%-5d ERROR: (For ch-%i) input buffers hold %u bytes, output buffers hold %u bytes, but %u was expected.
%25s:%-5d AUBeam2::ReverseMicChannelFlag is set to 0 (AU input mic order {back,front/side}, will flip mic order for BF kernel )
[%s|%s] Error with input stream format with error code %d
%s:%i Done initializing result = %i
%25s:%-5d clsp_enable_closed_loop default exists. Ignoring set property for EnableClosedLoop
[%s|%s] Unknown param id %u
%25s:%-5d kAUEndpointVAD3Property_DoneProcessingAudioForNonRealTimeDecode is write-only.
%25s:%-5d Block size for NNRES is not supported! Setting AU in Bypass mode.\n
[%s|%s] Number of channels %u in requested audio channel layout is different than in stream format. Default audio channel layout tag %s from preset is ignored.
[%s|%s] AUSM_HRIR: Generic HRIR is loaded from %s.
%25s:%-5d AUBeamNF: Error: Failed initializing Beam2N object
[%s|%s] %u incoming channel parameters dropped
%25s:%-5d Block size for NNNS is not supported! Setting AU in Bypass mode.\n
[%{public}.*s] scratch buffer too small for filter storage
[%p] AUReferenceSignal's property list \"Configurations\"[%u] has no \"Name\" key
[%s|%s] Setting input channel layout tag = %u (%s) failed - number of channels in layout (%u) is inconsistent with number of input channels (%u)
[%s] Params: Hopsize=%u, Blocksize=%u, Samplerate=%u
[%p] Successfully retrieved SmoothingFactor (%f).
%25s:%-5d Checking implementation cache.
[%p] failed to initialize - input format [%u %lf] and output format [%u %lf] mismatched 
[%s|%s] output type: %u
%25s:%-5d AUBeamNF::AUBeamNF (%p)
%s:%i failed to get processing graph %s delay latency property - %@
%25s:%-5d Successfully retrieved threshold (%g).\n
created
%25s:%-5d Successfully parsed the power smoothing time scales.
Failed to set AUDSPGraph graph test file path
%25s:%-5d MCLPOutSignals cannot be NULL. It is a required input.
%25s:%-5d EXCEPTION (%d) [activationFunction_ref.get_cf() == nullptr is false]: \"Failed to retrieve activation function (Function) from dictionary Activation.\"
[%{public}.*s] invalid filter size in bank attributes
%s:%i failed to create blending graph model
[%s|%s] Unsupported output channel count %u
%25s:%-5d AUBeamIt: Successfully initialized.\n
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve HangA01.\"
Register ControlFreak
<Updated Dezipper> Setting volume slider to: %.2f (%.2fdB). Current gain: %.2fdB - slider position: %.2f
[%p] Finished loading model plist
%25s:%-5d Error %i while restoring state
%25s:%-5d Loading SteeringVectorDictionary was not successful.\n
[%s|%s] ERROR: Could not create input capture file (no capture dir path available)
mInputGraphTensor is nullptr in getInputSize()
%s:%i failed to set processing graph %s property list property - %@
[%s|%s] Can't insert a new control point: not enough capacity
[%s|%s] updating dynamic XTC filters
mSimpleMeters failed to process; applying 20dB attenuation to this frame. (plist %s successfully applied | AU %s initialized)
VAD LPC block size %f ms is larger than %f
%25s:%-5d Failed to create new kernel at runtime: %s (err=%d)\n
%25s:%-5d EXCEPTION (%d) [outputDataType_ref.get_cf() == nullptr is false]: \"Failed to retrieve output data type (DataType) from dictionary OutputVectorDescriptor.\"
failed to set blending graph wet signal weight
%25s:%-5d Steering vector loaded from plist will be overwritten in the current mode. Current mode is (%d)
%25s:%-5d AUECMIMO: IQRD mode delay is set to %u samples.\n
[%{public}.*s] pre-allocated SRC conversion buffers for FP16 mode
%25s:%-5d InitCLParamsFromPlistV8
%25s:%-5d Error initializing EndpointVAD3: %s
%25s:%-5d AUNeuralNetSPP: (MCLPoutSignals, ECleeSignals, ECoutSignals) is NOT finite: (%u, %u, %u)
[%p] AU's block size (%d) not matching the NeuralNet's block size (%u). Will use a reblocker
[%p] will construct with M=%u, K=%u
[%{public}.*s] Error processing output SRC (%u)
[%s|%s] Logically invalid user data retrieved. Returning %s.
[%{public}.*s] transformation complete, %zu FD coefficients ready
[%s|%s] Update biquad mode selected
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataScale from dictionary OutputVectorDescriptor.\"
[%s|%s] Invalid output layout is defined for MatrixMix, resetting output layout = input layout
%25s:%-5d CircularModels: Target elevation not set to (%f), it remains at the current value (%f). Elevation should be in range [-90, 90].\n
failed to delete empty logs due to exception
%25s:%-5d SelectBeamsTo set to a value greater than number of beams. Setting it to mNumBeams-1.\n
Input bus must be mono\n
%25s:%-5d AUSpeakerProtectionV3::SetDefaultFormats\n
[%s|%s] ImmersiveRendererData failed to set the stream format for input %u, err = %d
[%s|%s] ImmersiveRendererData_V2: Error during common configuration, err = %d
%25s:%-5d Linn Data successfully set.
%25s:%-5d Wrong number of buffer lists!
%25s:%-5d Can't handle different in/out formats\n
[%s|%s] AUSMListenerPosition: LeftRight: %.4f, BackFront: %.4f, DownUp: %.4f
%25s:%-5d No anchor gains defined!\n
%25s:%-5d Cannot get HWParam key: %s
[%s|%s] Failed to set surround high shelf filters
%s:%i cleanup
[%s|%s] Instance is being destructed.
%25s:%-5d Using MIL function: %s
%25s:%-5d Identified Input Tensor: %s
%25s:%-5d Successfully parsed the power gain limit: %f
[%s|%s] Invalid or unhandled filter type
[%s|%s] Error scheduling unsupported parameter (control value) #%u: param = %u, scope = %u, element = %u
%25s:%-5d NeuralNetVAD: Loading DirectionalTargetElevation from topLevelDict.
SpatialBalance registered successfully
%25s:%-5d CADSPUtility:%s:%d: HOA Error; Trying to create a HOA rotation matrix of order = %d > 3 with FuMa normalization, capping to order 3
%25s:%-5d NeuralNetRES: Loading NumContextFrames from topLevelDict.
%s:%i failed to get processing graph %s latency property - %@
Buffers: EABL created
[%s|%s] Could not set reverb blend for group id = %u, err = %d
Register ToneMeister
%25s:%-5d AUBeam2::AUBeam2 (%p)
%25s:%-5d AUBeam2: Error: Beam object not initialized, won't dump post EQ
Error initializing FFT of size %u
%25s:%-5d failed to remove stale cache '%s': %s
%s:%-5d error creating PCM node with session ID: %llu
[%s|%s] Neural network has a sample rate = %u; input has a sample rate = %u --- initializing sample rate converters
[%s|%s] Number of channels %u in requested audio channel layout is different than in the stream format. Default audio channel layout tag %s from preset is ignored.
%25s:%-5d Input size of Prior_SPP  (%lu) is not equal to the the expected size  (%lu) or (%lu) is not equal to (%lu) (prop id: %u).\n
%25s:%-5d AUCircArray: (InputSignals) is NOT finite
%s:%-5d Invalid number (%u) of output buses requested. We only support 1–5 buses.
%25s:%-5d Failed to retrieve beam distance.\n
[%s|%s] ERROR: ImmersiveRendererData_V1 struct too small
[%{public}.*s] Processor was already initialized with a blocksize of %zu, bank mode %d
%25s:%-5d Initialize called without setting setting plist! Loading plist from path given by a defaults write
[%p] \n Kernel Plist: DelayStartBitsMsec %5.3f
[%s|%s] Critical Distance [m]: %f
[%s|%s] The computed ideal RT60: %f
[%s|%s] using ERSpatializer-provided split point for %s reverb: mixing time = %u samples
[%s|%s] ERROR: Unsupported ImmersiveRendererData version %u
NoiseGate registration failed
[ECv6] SetProperty(ECIR) rejected: inDataSize=%u not a positive multiple of sizeof(float) (mic=%u)
[%s|%s] ProcessMultipleBufferListsSlicingPrivate ERROR: result = %d
%25s:%-5d AUBeamNF Error: Invalid post eq data vector length from tuning file (expected %d bytes, actual %d bytes)
%25s:%-5d Invalid bass EQ sizes: BQ vector has %lu coefficients\n
[%s|%s] Toggling to MagLS filters
[%s|%s] Biquad Stage %u error %d; replacing with bypass filter
[%p] set 'mEnableImplementationCache' to %s
Setting Embedding failed (%d)
[%s|%s] Inconsistent behaviour: there was already an input capture file! Disposing of it.
AUDSPGraph registration failed
%25s:%-5d Error encountered while creating deep copy of filter dictionary
%25s:%-5d ReverbSuppressor object failed to instantiate; AU going into soft bypass mode.
Preference: '%s %s' does not exist.
%s:%i failed to create blending graph - %@
%25s:%-5d Error initializing EndpointVAD2: %s
[%s|%s] Capture directory exists but is not writable: %@
%25s:%-5d Volume Map component is not in increasing order: %s. Reversing the order.
%25s:%-5d Internally set the Kalman process variance as (%g).
%25s:%-5d Successfully loaded NeuralNetRES plist.\n
%25s:%-5d EXCEPTION (%d) [ioStates_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputOutputStates.\"
%25s:%-5d MIL2BNNS Destroyed mContext.data
%s:%i Setting zoom amount %f on mDominanceZoom
%s was reset without initialize
[%s|%s] ImmersiveRendererData could not set the layout (tag = %u) for input #%u, err = %d
%25s:%-5d Successfully retrieved number of Ref Levels (%i).\n
ioOutputBufferLists[%u]->mNumberBuffers=%u, ASBD::NumberChannelStreams(output.GetStreamFormat())=%u; kAudio_ParamError
%25s:%-5d Compiling graph
[%p] Successfully loaded NeuralNet plist.
[%s|%s] update called for input #%d, number of inputs = %u
%25s:%-5d Volume Output Map: %s
%25s:%-5d AUDereverb: Using logPeriod of (%g)s as specified in defaults write mclp_log_period_in_seconds.\n
%25s:%-5d AUBeamNF: Error: Failed setting diffraction filter and post EQ
%25s:%-5d graph workspace size is %zu bytes
%25s:%-5d AUSpeakerProtectionV3::SetProperty - EnableClosedLoop %s->%s\n
[%{public}.*s] LSBank: start of fadeout is before window fadein
[%p] NeuralNet initialization using plist in AUNeuralNet failed with %s error %d: %s
%25s:%-5d Loading NumContextFrames from topLevelDict.
%25s:%-5d Embedding name not found, using empty.\n
%25s:%-5d AUECMIMO: energy measure in [dB] for ref-channel %u : %f\n
%25s:%-5d Ch %d, CLParams:\n%s
%25s:%-5d Successfully parsed the power amp efficiency model: [ %s ]
%25s:%-5d AUBeam2: Error: AUBeam2N should have property kAudioUnitProperty_UsesFixedBlockSize set to 1 before initialize
[%s|%s] Error: this output layout is invalid
[%s] Sync synthesiser initialisation complete (%.2f ms)
%25s:%-5d Set TransducerCalibrationCF property
[%s|%s] Distance Attenuation: Failed to set the attenuation law
%25s:%-5d MultiRadixRealFFT_RealInPlaceTransform() returned an error.
parseTwoPointCurve() Error: expected two numeric values
[%p] created NeuralNet instance in %lld milliseconds
%25s:%-5d Graph model is null: %@
[%s|%s] Configuration does not support personalized HRTF.
[%s|%s] failed to create neural network input SRC with error code %s
[%s|%s] ImmersiveRendererData does not provide a channel layout, using the default channel layout for the given number of channels
%s:%i show internal params set to %u
[%s|%s] AUSMTrackedHeadPose: Error %d in getting head-pose.
[%s|%s] could not set the spatialization algorithm with output type %u
%25s:%-5d Getting property info for CurrentBeamCoeffs failed (prop id: %d).
%25s:%-5d 'ReverbTails' dictionary found in Plist.
%25s:%-5d Invalid camera direction %u
[%p] Setting property Bitstream_CF (prop id: %d).
%25s:%-5d Create DOA-based estimator\n
%25s:%-5d Failed to retrieve number of coefficients.\n
[%s] Loaded a set of %u HRIRs, with length=%u samples.
%25s:%-5d AUNeuralNetVAD: (InputSignals) is NOT finite: (%u)\n
%25s:%-5d AUECSUMO: ********* Reset begins *********\nAUECSUMO: state variables have finite values (1 if True): %u\nAUECSUMO: ref-signal buffers have finite values (1 if True): %u\nAUECSUMO: EC output buffers have valid values (1 if True): 
%s %s: aufx %s appl created; using ProcessMultiple
%25s:%-5d AUNeuralNetRES: Successfully Initialized.\n
[%p] failed to reset graph - %@
[%{public}.*s] initialized at %uHz
[%s|%s] Unexpected Ambisonics format
%25s:%-5d Failed sparse_matrix_vector_product_dense_float for %s.\n
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve forgetting factor Lambda_TC.\"
%25s:%-5d  Unable to instantiate VarEQ AU
[%s|%s] invalid wall ID
[%s|%s] error %d while initializing source extent processor
%25s:%-5d mProcessWasCalled: %u\n
[%s|%s] Source extent processor is loaded with incorrect configuration. Spatializer will ignore source size.
Essential plist parsing did not succeed before initialization; applying 20dB attenuation until *successfully* reinitialized. (AU %s initialized)
[%s|%s] Updating attributes for %s reverb
%25s:%-5d  could not get processorSubType string
%25s:%-5d Fmin must be < (samplingRate/2). Setting Fmin = samplingRate/2.\n
[%s|%s] Setting HOA bypass matrix for W passthrough
[%p] created audio capture file: %@
Invalid format detected
%25s:%-5d MIL2BNNS: Exception in BNNSGraphContextDestroy!
[%s|%s] Couldn't find a matching preset. Returning %s.
[%s|%s] ImmersiveRendererData could not set the source mode to point source for input %u, err = %d
[%p] failed to process graph - %@
%25s:%-5d EXCEPTION (%d) [inputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputName from (%s).\"
[%s|%s] Mismatched frequency resolutions between the requested room config and user data. Returning empty optional.
[%s|%s] ImmersiveRendererData: %u channel infos retrieved
%25s:%-5d Kernel created successfully.
%25s:%-5d AUBeam2: Error: Beam object not initialized, won't dump diffraction filter
%25s:%-5d BorrowSubbandDOA failed, subband DOA calculator is not initialized.
[%p] failed to initialize - parameter mix frequency must not exceed Nyquist frequency
[%s|%s] Invalid number of channels and/or sample rate
%25s:%-5d The number of channels in the input format (%u) is not equal to the number of mics the beamformer expects (%u).\n
%25s:%-5d MIL2BNNS cache file '%s' %s
CMDeviceState orientation error on %s: %{public}@
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve ECleeScale.\"
failed to run processing graph
%s: error %d getting input stream format of %s
%25s:%-5d about to throw %s: %s
%25s:%-5d context size is %zu bytes
%25s:%-5d Successfully retrieved number of mics used (%i).\n
%25s:%-5d CPMS power gain group: [ default ]
%25s:%-5d Failed to parse speaker calibration data
[%{public}.*s] AULeanSpatial: headtracker ON
[%s|%s] AUSM_VERBOSE|CommonGrid #%u: %s
Failed to set AUSpatialMixer output channel layout
[%s|%s] NeuralNet initialization using plist with assumed base path failed with an unknown exception.
[%{public}.*s] LSBank::getDataIndex(): input indices out of bounds
[%s|%s] Found user defaults %s in overrides
%25s:%-5d SubbandDOA not set. Input size (%u) and internal size (%lu) do not match.\n
%s:%-5d Invalid number (%u) of output buses requested. We only support 1–2 buses.
%25s:%-5d AUSpeakerProtectionV3::ApplyParameters(): Params up to date. paramSeed=%d; mParamsUpdated=%d
%25s:%-5d Setting new FIR matrix
%25s:%-5d Found the dictionary RealCoefficients.\n
%25s:%-5d AUBeam2::Cleanup (%p)
%25s:%-5d Failed to find beamformer box or coefficients dictionary!
%25s:%-5d AUBeamNF Error: Converting mic spacing from tuning file
DynamicIRProcessor: Reconfiguring IRProcessors
[%{public}.*s] no state space provided: pre-allocated internal transformed coeffs storage (%zu bytes)
%25s:%-5d Initializing with PowerBudget: [ %s ]
[%s|%s] Invalid parameter(s).
%25s:%-5d Found the dictionary OutputVectorDescriptor.
[%p] NeuralNet initialization using plist in AUNeuralNet failed with runtime_error %s.
%25s:%-5d CPMS power control is %s loop
[%s] Configured filterbank with %u frequency bands (of which the first %u bands will be processed)
[%s] Loaded HRIRs have different a different samplerate to the host/DAW samplerate
[%s|%s] Error %d setting property %u to element %u
[%s|%s] Reusing cached MagLS decoding filters
[Room Congruence] %s: Room configuration invalid - arrays should have the same number of elements.
NonMediaChatDynamicDuckingEnabled: invalid propery size
%25s:%-5d PilotAmplLo limited to %f
[%p] Successfully retrieved batch size (%u).
[%s|%s] Initializing %u channel processors
%25s:%-5d Starting Initializing with %d ins, %d outs\n
%25s:%-5d GetPropertyInfo ID=%d scope=%d bus=%d\n
%25s:%-5d Ch %d; T_CL=%6.2f; T_OL=%6.2f; TlimAdj=%6.2f; DGain=%5.2f; TGain=%6.4f; tgtgain=%4.2f, hlimgain=%f, sReb=%f
%25s:%-5d EXCEPTION (%d) [nnLayers[i].mWeightsQuantized.size() != weightsNumberOfCoefficients is false]: \"Number of weights in Data (%lu) does not match the required number of weights (%lu).\"
[%{public}.*s] process error, too many frames to process (requested %u, max %u)
%s:%-5d Signal name set by user : %s
SetProperty( kAudioUnitProperty_DspLibDictionary ) Error: unknown plist format\n
[%{public}.*s] allocated internal FP16 conversion buffers (%zu bytes)
%25s:%-5d Setting up box %s
%s:%i failed to set processing graph %s preset property - %@
%s:%i tuning dir path: %s
[%p] Loading lookahead size from plist.
[%s|%s] Setting input bus count = %u
[%s|%s] Resetting auto mode reverb
[%p] failed to locate austrip file - %s
%25s:%-5d allocation for tensor name: %s nBytes: %zu
[%s|%s] No existing room preset, using input preset.
Failed to set new music austrip on AUDSPGraph
[%s|%s] Neural network has valid %u output channels; assuming FOA passthrough mode
AUEchoGateV3: Non Finite input buses found with bit pattern (%lu). Will produce silence if used in the signal path.\n
[%s|%s] Setting reverb send decorr filter coeffs on Input Element %u to %u:
AUSpatialMixer Initialize() failed with exit code %d
[%s|%s] Updating crossover for ScottyUpmixer
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Beta from dictionary Activation.\"
[%{public}.*s] LSBank: length of fadeout is greater than filter
%25s:%-5d Noise suppressor failed to process.
%25s:%-5d Fmin must be <= Fmax. Setting Fmin = Fmax.\n
%25s:%-5d Failed to create new kernel: %s (%d)\n
[%{public}.*s] failed initializing convolver (error=%u)
[%{public}.*s] failed to initialize fractional delay line %u
%25s:%-5d Failed to set SelectBeamsTo parameter: %@
%s:%i BypassEffect state unchanged: %d
[%s|%s] Switching from ProcessMultiple to Render without reinitializing
%25s:%-5d Fmt%u: %s
[%s|%s] Could not %s exclusion zone on group %u, err = %d
[%p] Construct AU
[%s|%s] error %d setting preset on %s
%s: error %d setting output stream format %s for %s
%25s:%-5d Loading MCLPOutScale from topLevelDict.
%25s:%-5d NeuralNetVAD: Loading HangA01 from topLevelDict.
%25s:%-5d AUSpeakerProtectionV3::Cleanup
[%s|%s] Could not wait for reverb, err = %d
%25s:%-5d Resetting the AU.
%25s:%-5d Acting on invalid ThermalMeasurementType
[%s|%s] MagLS load time = %.2f ms
%25s:%-5d Successfully called sparse_matrix_vector_product_dense_float for %s.\n
  from %s, render err: %d
processing graph not initialized
[%s|%s] Creating %s orientation observer
%25s:%-5d BeamformerCoeffs successfully set.
%25s:%-5d EXCEPTION (%d) [layer.mBiasVector.size() != weightsSizeOutput is false]: \"NeuralNetBNNS: Layer (%u), bias size (%lu) is not matching the weight output vector size (%lu).\"
[%s|%s] EABL ingestion: mFirstAudioBufferSampleTime (%d) = mdFrameHeader->frameStartTime (%d) + mPImpl->mSaveTrimmedSamplesFromBeginning (%d) + mdEvent->eventStartTime (%d)
[%s|%s] Could not set directivity index %u for group #%u: err = %d
%25s:%-5d AULoudnessInNoise: Initialize
%25s:%-5d AUSeparate: Cleanup.\n
%25s:%-5d Error setting parameter %u: %@
%25s:%-5d Error setting orientation parameter: %@
[%s|%s] Directory created for capture: %@
%25s:%-5d Sampling rate in the plist (%g Hz) does not match the actual sample rate (%g Hz). Setting the AU in bypass mode.
[%s|%s] Invalid spatialization algorithm %u
[%s|%s] Failed creating HOA decoders: arrays sizes don't match or are empty. Defaulting to stereo
%25s:%-5d AUDereverb: parameters changed after Initialize, which will allocate memory on the realtime audio thread - only SetParameter before Initialize.\n
%25s:%-5d Enabling recording
[%s|%s] Cannot render with ProcessMultiple since the samplerate of the input element %u is %f whereas the output samplerate is %f
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"ECOutScale not loaded.\"
destroyed
%25s:%-5d AUSpeakerProtectionV3::~AUSpeakerProtectionV3
%25s:%-5d Failed to retrieve number of Ref Levels.\n
%25s:%-5d Successfully retrieved weights data (%i) at index (%zu).
%25s:%-5d CADSPUtility:%s:%d: HOA Error; HOA object was not initialized
blending graph not initialized
%25s:%-5d Preparing BNNS NeuralNet implementation.
[%s|%s] Custom Bypass Matrix found in IR file
%25s:%-5d AUBeamNF::SetDiffractionFilterAndPostEQ (%p)
[%s|%s] Failed to set high pass filter coefficients
%25s:%-5d Failed to load the number of filter coefficients from the plist.\n
Initializing...
[Room Congruence] %s invalid - the %s array is empty.
%25s:%-5d AUBeam2: Error: Failed initializing Beam2 object
%25s:%-5d Tuning name '%s'
[%s|setProperty] (scope=%u, element=%u): %s not writable after the AU is initialized
%25s:%-5d Successfully loaded NeuralNetVAD plist.\n
%25s:%-5d Setting property EnableSubbandDOACalculation to %d (prop id: %d).
%25s:%-5d MIL2BNNS Deallocating mGraph.data from MIL
[%s] Initialising container with %u frequency groups, %u hops, and %u maximum number of DoAs
%25s:%-5d InitCLParamsFromPlistV7
%25s:%-5d %s TargetUI orientation (%u): %s (%f)
[%s|%s] Looking for user defaults %s
[%p] destructed
[%p] Successfully retrieved HangoverOffSetFrames (%u).
[%s|%s] Updating HRTFHQ reverb
%25s:%-5d Loading KalmanProcessStd from topLevelDict.
%25s:%-5d AUECSUMO: ********* Logging ends *********\n
[%s|%s] Early length = %u
%s:%i create blending graph (deferred)
%25s:%-5d Info for unsupported property (%u) requested.
[%p] Input and output sample rate do not match
Trying to set embedding value, but embedding buffer is not available.
[%{public}.*s] Failed to re-initialize shared late processor with state memory
%25s:%-5d Successfully parsed all %lu ignore-telemetry params.
[%s|%s] Error %d setting Diffuse on group %u
ControlFreak registered successfully
[%s|%s] invalid element = %u for input scope property = %u
[%s|%s] the PlaybackRate parameter value can only be 1.0 with ProcessMultiple as the render method
%25s:%-5d mNumberOfChannels: %u\n
[%p] failed to initialize DSP graph - %@
[%s|%s] Could not set the post-processing reverb blend to 50 on input %u, err = %d
[%s|%s] TuneTarget failed. Returning %s.
[%s|%s] Number of outputs does not match with desired HOA order; reducing order, only %u channels will be active (others muted)
[%s|%s] Could not acquire the lock. Vertices and gains not incremented.
[%{public}.*s] late reverb dataOffset (%zu) must be < partition size (%zu) - current deferral implementation limitation
%25s:%-5d Failed to set real-time safe mode on matrix
%25s:%-5d AUECMIMO: ********* Reset begins *********\nAUECMIMO: state variables have finite values (1 if True): %u\nAUECMIMO: ref-signal buffers have finite values (1 if True): %u\nAUECMIMO: EC output buffers have valid values (1 if True): 
%25s:%-5d Time-frequency smoothing update failed
Sample rate mismatch (mic = %f, ref = %f, eclee = %f, out = %f)
stop migrating AudioUnit assets
[%s|%s] ImmersiveRendererData: Could not configure %u (%s) renderer type (2), input #%u, err = %d
[%s|%s] dispatching update for all InputElements
%25s:%-5d mFrequencyDomainInput: %u\n
%25s:%-5d AUECMicRef: ERLE measure in [dB] for mic-channel %u , internal: %f (dB), external: %f (dB)\n
%25s:%-5d failed to allocate %d page aligned bytes
%25s:%-5d EndpointVADDSPChain: Incorrect threshold multiplier LUT format in the Plist.
%25s:%-5d Number of channels on the output bus in not matching the expected number of channels (%u).\n
set up logs in \"%s\"
%25s:%-5d Maximum frequency for frequency dependent shape decay must be lower than maximumfrequency. Using fixed shape parameter instead of frequency depedent one.\n
%25s:%-5d kAUEndpointVAD2Property_EndpointerSpeechDetectionEvent cannot be directly accessed.
VAD LPC order is %d
[%p] ModelNetPathBaseOverride is set to null and thus removed
%25s:%-5d The CFStringRef passed to SetProperty is null.
%25s:%-5d Locking orientation at %s (%i)
[%s|%s] Could not initialize bypassable IR processor
%25s:%-5d AUECSUMO: Using logPeriod of (%g)s as specified in defaults write ecsumo_log_period_in_seconds.\n
%25s:%-5d AUDenoise: Cleanup.\n
SetProperty( kAudioUnitProperty_DspLibDictionary ) Error: AU has zero channels, uninitialized?\n
%25s:%-5d 'ReverbTails' dictionary is not present in Plist.
[%s|%s] Error scheduling unsupported parameter (immediate) #%u: param = %u, scope = %u, element = %u
Setting bypass property to %u
dlerror : libAudioIssueDetector ADAM: %s
[Room Congruence] %s invalid - missing or wrong type for %s.
[%p] Using low delay block processor with delay = %d samples.
[%p]  %u
%25s:%-5d Can't handle more than 4 input channels\n
%s:%i cannot process %u I/O channels with %u channel DSP and batch size %u
[%p] will initialize with configuration: %s
[%s|%s] From PHASE input: mid-band RT60 = %.3f s, room volume = %.1f m3
%s:%i ----
IV data format not supported. But this should have been caught earlier
[Room Congruence] %s: The low cut input RT60 for warping must be lower than the high cut RT60. Returning empty optional.
[%s|%s] MetadataSetParameter param = %u, scope = %u, element = %u, value = %f, offset = %d, duration = %u
%25s:%-5d Lock requested while already locked?!
[%s|%s] Override for user defaults = %s has incorrect value.
[%p] AUReferenceSignal's property list \"Configurations\"[%u] has no \"Gains\" key
[%s|%s] inData == nullptr
%25s:%-5d Requested batch size for NeuralNetCache (%u).
[%{public}.*s] constructed %lu-bit processor (external/internal) = (%uHz/%uHz)
[%s|%s] Cleaning up TorqueEngine
[%s|%s] PMBLSP return an error %d
%s %s: could not instantiate aufx %s appl
[%s|%s] ERROR: not initialized
%25s:%-5d Input size of SpatialProbabilityInputSourceProbability_CF is not equal to the expected size (prop id: %u).\n
[%s|%s] Spatial audio over built-in speakers not available on this hardware (no XTCIR); reverting to VBAP panning using output channel layout tag = %u (%s) with %u channels
%25s:%-5d EndpointVADSegmentHeuristics: Transition state value not found in the history buffer!
[%p] I/O formats are not compatible.
[%p] will try to initialize
%s
[%s|%s] ERROR: could not initialize the cartesian panner #%i with channel layout tag %u: err=%d
[%p] VAD is %s
VAD max periodicity tracking frequency %f Hz is greater than %f
[%{public}.*s] requested number of output channels (%zu) exceeds available coefficient channels (%zu)
[%s|%s] Error creating neural network - Neuralizer plist does not exist: %s
%25s:%-5d Could not load NeuralNetRES plist, exception (%d).\n
[ECv6] LoadPendingIRsFromDictionary: missing/invalid NumMics/NumRefs/FilterSize (got NumMics=%u NumRefs=%u FilterSize=%u)
[%s|%s] Could not get personalized HRTF status. Error: %u. Assuming generic HRTF is being used.
[%s|%s] XTCIRFileList error or empty list
[%p] number of media output buffers %u is not equal to expected number of media output channels %u
[%s|%s] NeuralNet initialization using plist failed with an unknown exception.
[%p] channel map is not set (AU will use default channel map instead)
[%s|%s] Could not set BCM LFE low pass frequency
parseDictionary() Error: mainCurve element %u is not numeric
%25s:%-5d Setting graph slice timing: max slice duration %u, fs %u
%25s:%-5d NeuralNetRES: Loading forgetting factor Lambda_TC from topLevelDict.
[%s|%s] Setting input properties
%25s:%-5d Error reading AbsoluteSilenceThdDb from AGC plist dictionary.
%25s:%-5d Ignoring telemetry, as: [ %s ]
AUNeuralNet registration failed
%25s:%-5d The number of input channels not equal to the number of expected channels (%u).
%s:%i error %i while restoring state
%s:%i will setup internal CAReporterID
[%s|%s] invalid optional feature dictionary.
%25s:%-5d Missing scalar %s.\n
[%p] \n Freq Interval %u  Freqs are: 
failed to calculate expected processing graph output frame count
%s:%i failed to load 'AUNeuralNet' property list
%s:%i create blending graph
%s:%i loading from %s failed, caught unknown exception
[%p] Successfully retrieved sample rate (%g Hz).
[%s|%s] invalid scope = %u for input scope property = %u
[%s|%s] [InputElement #%u] Error setting audio channel layout: null layout pointer
%25s:%-5d  could not get parameter value
failed to set blending graph dry signal weight
[%p] Failed to retrieve batch size, default to 1.
[%s|%s] AUSM_VERBOSE: %s, dirAz=%.1f, dirEl=%.1f
[%p] failed to set DSP graph parameter %u
[%p] failed to apply %s at %s with resource path %s - error %@
%25s:%-5d CPMS power controller is %s
%25s:%-5d AUSpeakerProtectionV3::Reset
[%s|%s] Invalid output type %u with useOutputType algorithm
[%s|%s] Sample rate is zero
Running Constructor...
%25s:%-5d Detailed logging set to %d.
[Room Congruence] %s: Both low and high cut output RT60 for warping must be greater than 0. Returning empty optional.
%s:%i only first order is supported now
[%p] \n Kernel Plist: EnableChirpPolarity %u
%25s:%-5d Internally set the Kalman observation variance as (%g).
[%p] updating DSP graph parameter %u: %f -> %f
[%s|%s] FallbackSPAD: inconsistent sizes
[%s|%s] Could not enable the PP reverb: err = %d
Media Chat: setting unducking ramp time %.2fs
ECv6: partial mic processing nProcMics=%u mNumMics=%u (micChans=%u outChans=%u); higher mics will stale
%25s:%-5d Fixed number of graph output ports different from expected: %u
%25s:%-5d Parameter PilotLowerThres greater than PilotUpperThres. Set PilotLowerThres = %f
[%s|%s] cannot change bus count for scope = %u
[%s|%s] auto mode reverb not initialized
[%s|%s] AUSMTrackedHeadPose: Y: %.2f, P: %.2f, R: %.2f, Quat: (%.4f, %.4f, %.4f, %.4f. Error = %d)
NumInputElements not consistent with inNumberInputBufferLists
Unregistering device orientation observer %s
[%s|%s] Capture file: %s
%25s:%-5d DirectionalModelConditionalTargetPrior not found, being set to (%g).\n
%s:%-5d input and output formats do not match
%25s:%-5d Failed to set BeamSystemNoiseProfile data to SpectralProfile object. Invalid dictionary entry?
Setting ProtectionLevel to %s
[%s|%s] Updated surround filters ---- suroundEQAmount = %f, highShelfGaindB = %f
[%{public}.*s] failed to initialize MDF convolver for BRIR/LATE (freqDomain=%d, bankMode=%d)
[%s|%s] Setting reverb send decorr filter lengths on Input Element %u to %u:
%25s:%-5d Input kappaMin must be lower than kappaMax. Skipping updating model with Prior weighted frequency dependent shape parameter.\n
VAD min periodicity tracking frequency %f Hz is less than %f
%25s:%-5d Bad ref mic for limit wind boost %i
%25s:%-5d  Input volume curve is not monotonic. %s
%25s:%-5d Preparing Espresso NeuralNet implementation.
[%s|setPropertyDictionary] (scope=%u, element=%u): invalid property ID %u
%25s:%-5d Plist has unknown outputChannelLayout. Using Binaural by default
[%s|%s] Sample Rate can not be zero
%s:%i AUDenoise registration failed
[%s|%s] [OutputElement] Setting audio channel layout %s
start migrating AudioUnit assets
%25s:%-5d Override SpCl Property with defaults clsp_srdc_r %f
[%s|%s] AudioFormatExtended metadata ingestion is not functional
[%s|%s] Too many parameters for ProprietaryStaticData
Failed to set dialogue TM dictionary property
[%s] Loading ATFs failed.
%25s:%-5d LPCore::UpdateLPC: Arguments cannot be null
%25s:%-5d Successfully retrieved ECleeScale (%g).\n
%25s:%-5d (InputSignals) is NOT finite: (%u)\n
%25s:%-5d NeuralNetVAD: Loading FFT2Mel matrix from topLevelDict.
[%s|%s] Could not enable the PP ERs: err = %d
[ECv6] SetProperty(ECIR) rejected: inElement=%u exceeds kAUEchoCancelerV6_MaxMics=%u
%25s:%-5d CADSPUtility:%s:%d: VBAP Initialization Error; Check for duplicate vertices
[%{public}.*s] AULeanSpatial: destructed
[%p] NeuralNet initialization using plist in AUNeuralNet failed with exception: %s
[%p] Successfully retrieved HangoverOnSetFrames (%u).
%25s:%-5d Initialize DOAConditioner with time smoothing (%f) and frequency smoothing (%f).\n
[%s|%s] ImmersiveRendererData failed: too many channels for rendererDescription #%u
[%s|%s] Could not set the post-processing reverb blend to 0 on group id = %u, err = %d
AGC VAD sample rate converter produced %u output frames for %u input frames with maximum block size of %u frames
[%{public}.*s] no state space provided: pre-allocated internal next coeffs storage for crossfade (%zu bytes)
%s:%i interal CAReporterID successfully initialized
[%p] Successfully retrieved ProbabilityThreshold (%f).
[%s|%s] 
[%s] Failed to load HRIRs.
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"LambdaPSD_TC not loaded.\"
[%s|%s] ImmersiveRendererData failed to enable input #%u, err = %d
[%{public}.*s] storage size mismatch for FD coefficients (have %zu, need %zu)
%25s:%-5d Failed to load the sampling rate from the plist.\n
%s: Temp directory string: %s
%25s:%-5d Attempting to set data for property %u (%s)
[%s|%s] Custom Bypass Matrix gain vector was not found for input channel label = %u
%25s:%-5d AUBeamNF: Error: AUBeamNFN should have property kAudioUnitProperty_UsesFixedBlockSize set to 1 before initialize
[%p] fftSize = %u, maxFramesPerSlice = %u, usesFixedBlockSize = %u
%25s:%-5d AUECMicRef: energy measure in [dB] for ref-channel %u : %f\n
[%{public}.*s] process error, caller provided too few output buffers (provided %u)
%25s:%-5d AUBeam2 Error: Invalid mic spacing %d
%s:%i BypassEffect state changed to: %d
[%s|%s] Invalid preset.
%25s:%-5d EXCEPTION (%d) [modelNetPathBase_ref.get_cf() == nullptr is false]: \"Failed to retrieve ModelNetPathBase.\"
[%s|%s] Failed to initialize Delaunay triangulation.
[%s|%s] Provided vector of parameters does not match size of SoundStage parameter vectors.
%25s:%-5d AUBeam2: Error: Could not read post EQ file %s
%25s:%-5d AUBeam2::DumpDiffractionFilter (%p)
[%p] Block size for model: %s is %f
%25s:%-5d AUSpeakerProtectionV3::SetParamDefaults
%25s:%-5d Internal decision history buffers must have the same size
%25s:%-5d Bind buffers for input and output states.
%25s:%-5d Successfully retrieved beam distance (%0.2f).\n
[%s|%s] ImmersiveRendererData failed to set the source orientation reference for input #%u, err = %d
MeisterStueck registered successfully
[%{public}.*s] using pre-transformed frequency-domain coefficients
%25s:%-5d Setting up beamformers
%25s:%-5d MultiRadixFFT_Create() returned an error attempting to create mCplxFFTSetup_Long. Invalid block size?
[%p] NeuralNet's number of output channels (%u) times batch size (%u) not matching AU's number of output channels (%u).
[%s|%s] Could not initialize source extent processor, Spatializer will ignore source size.
%25s:%-5d AUECSUMO: ********* Window Initialized *********\n
%25s:%-5d NeuralNetVAD: Loading CombinedProbabilityMode from topLevelDict.
%25s:%-5d MIL function is non-default: skip primary cache IR
Failed to initialized AUDSPGraph
[%s] Iterative grid scanning will first scan %u sparse directions
%s:%i DenoisePresetPath is overridden to %s
[%p] AU not initialized: Cache embedding vector
[%s|%s] Invalid max frames per slice: %u
%25s:%-5d AUECMIMO: Initialize.\n
%25s:%-5d NeuralNetVAD: Loading OutputMaskMode from topLevelDict.
compiled \"%s\"
parseDictionary() Error: value for key '%@' is not an array
[%s] Disabling coherent focussing
[%p]  %5.3f
%25s:%-5d Successfully retrieved ECOutScale (%g).
%25s:%-5d AUBeam2::SetDiffractionFilterAndPostEQ (%p)
%25s:%-5d %s does not have zoom curve
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"InputChannelCounts\"][%u] has invalid value
[%s|%s] invalid input scope element = %u (property = %u)
[%s|%s] Not a valid tag for Ambisonics SoungStage (must be FOA): Tag = %s, number of input channels = %u
CFURLPropertyCStringInterface::%s: file %s not found
%25s:%-5d Could not initilize kernel\n
[%s|%s] Failed to compute the critical distance gain biquad. Returning empty optional.
[%{public}.*s] delay value stored (%zu samples) but not applied (zero-delay mode)
[%p] Could not create NeuralNet model using the plist, exception %d
%25s:%-5d EXCEPTION (%d): \"Unknown value for mType (%u).\"
%25s:%-5d AUDereverb: ********* Logging begins *********\nAUDereverb: logging (period, timestamp): (%f, %f) (s)\n
%s| Invalid dictionary
%25s:%-5d Preset does not match AU version. Skipping RestoreState
%25s:%-5d Could not fully parse the EnableCPMSControl param. Will use the default.\n
[%s|%s] Unknown data location index %u
%25s:%-5d Found the dictionary Bias.
[%s|%s] could not initialize the channel processors with output type %u
%25s:%-5d GetProperty ID=%d scope=%d bus=%d\n
%25s:%-5d AUSpeakerProtectionV3::AUSpeakerProtectionV3
%25s:%-5d Successfully retrieved output data type (%s) for Layer %u.
%25s:%-5d AUNeuralNetSPP: (OutputSignals) is NOT finite: (%u)
%s:%i locked
%25s:%-5d AUSeparate: (OutputSignals) is NOT finite: (%u)\n
[%s|%s] AUMonopoly does not support multiple center channels - Duplicate center label
%s:%i DenoiseEnable set to: %u
%s is bypassed. Reason: host IO cycle duration = %.3f, Minimum IO cycle duration required by AU = %.3f)
%25s:%-5d StreamingMode set to (%d).
%25s:%-5d Component info: %s %s %s
%25s:%-5d AUEndpointVAD: The model dictionary property is unset (required).
%25s:%-5d nnSoftVAD has value (%f). Valid range is [0, 1]. Skipping update.\n
[Room Congruence] %s: Both low and high cut input RT60 for warping must be greater than 0. Returning empty optional.
[%s|%s] Number of input channels inconsistent with number of labels for layout = %u (%s)
[%s|%s] Error writing input data to file, %d
[%s|%s] Error: not enough group config elements
[%s|%s] Applying
%s: %s for factory preset #%d not found
%25s:%-5d Loading nMicsUsed from topLevelDict.\n
%25s:%-5d EXCEPTION (%d): \"Unsupported activation function.\"
[%s] non-media-chat dynamic ducking
[%{public}.*s] Failed to initialize source slot %zu
%25s:%-5d Part AUSpeakerProtectionV3::SetParameter(%d): partElement is null\n
[%p] Weighting for Speech Probability mask has %d elements
[%s|%s] Can't fetch the current parameter value
[%s|%s] Could not get personalized HRTF status.
%25s:%-5d AUECMicRef: Reset.\n
[%s|%s] Using library room IR %d
%25s:%-5d EXCEPTION (%d) [biasDataType_ref.get_cf() == nullptr is false]: \"Missing dictionary DataType from dictionary Weights.\"
total latency is %f seconds
%s:%i NeuralNetModelNetPathBaseOverride is set to null and thus removed
[%s|%s] Could not reconfigure auto mode combined late reverb: error %d
[%s|%s] Number of channels = %u in AudioChannelLayout does not match number of channels = %u in stream format.
%25s:%-5d AUBeamNF::SetParameter (%p): id = %d, scope=%d, element=%d, inValue = %f
[%s|%s] Constructing : sample rate = %f, frame size = %u
[%p] cannot process %u input channel streams (expected channel stream count is %u)
[%{public}.*s] cannot create source - all %zu slots in use
[%s|%s] Failed to initialize reverb
%25s:%-5d Input size of SpatialProbabilityInputSubbandDOA is not equal to the expected size (prop id: %u).\n
%25s:%-5d Successfully retrieved mVADinAudioOutputMode (%u).\n
%25s:%-5d Failed to set new config plist: %s (%d)\n
%25s:%-5d CLSPKernel_v5::CalcCoeffs
[%s|%s] Sample rate must be greater than zero
%25s:%-5d CADSPUtility:%s:%d: HOA Error; This is not SN3D/N3D/FuMa: unsupported
%25s:%-5d Initializing graph
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Gains\"][%u] has no \"Input\" key
[%p] Finished finding models. Found (%u) models
%25s:%-5d Embedding name set to (%s).
%25s:%-5d External Shape Parameter Per Frequency property was set, but it is not used in the current mode. Current mode is (%d)
[%p] I/O formats are not compatible
[%s|%s] Unknown ASC type %u
[%s] Using the full scanning grid (%u directions)
%25s:%-5d !mGraph
[%p] Current bits assumed (%u total): 
[%s|%s] scope = %u, element = %u
[%{public}.*s] source destroyed (inactive)
[%p] DSPGraph output bus format: %s don't match expected format: %s
%25s:%-5d AUBeamIt: Cleanup.\n
Initialization complete.
%25s:%-5d Found the dictionary Activation.
RTDebugLogger: ring buffer would be %zu MB (cap 8 MB) — reduce registered slots or filter length
[%p] AUReferenceSignal's property list has no \"Configurations\" key
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"InputChannelLayouts\"][%u] has insufficient byte size
%s:%i will try to register internal AUs
[%s|%s] NeuralRAD network being loaded...
%25s:%-5d Input size of SpatialProbabilityInputPostMask_CF is not equal to the expected size (prop id: %u).\n
[%{public}.*s] destroyed all sources
[%p] check output format before initialization
%25s:%-5d Successfully retrieved the time constant for PSD (%g).
[%s|%s] Could not set parameter %i immediately - Not Found
[%p] DSPGraph (%d -> %d) I/O bus counts don't match expected (1->1) bus configuration
[%s|%s] AUSM_VERBOSE|ReverbIRWeights[%u]={%s}
%25s:%-5d AUSpeakerProtectionV3::Initialize\n
[%s|%s] AUSMHeadOrientation: Y: %.2f, P: %.2f, R: %.2f, Quat: (%.4f, %.4f, %.4f, %.4f)
[%s|%s] Can't insert a new track: not enough capacity
%25s:%-5d AUECSUMO: ********* Window not initialized: returning error *********\n
Set metadata blob with CFDataRef
%25s:%-5d NeuralNetRES: Loading BlockSize from topLevelDict.
%25s:%-5d Pointer size of SpatialProbabilityInputShapeParameterPerFrequency_CF is not equal to the expected size (prop id: %u).\n
[%{public}.*s] output channel count mismatch (got %zu, expected %u)
Failed to set pack immersive render data: %s
Failed to open headphone preset
%25s:%-5d Failed to retrieve %s.
[%{public}.*s] destructed
%25s:%-5d No RW permission to temp path: %s
Failed to set AUSpatialMixer immersive render data
[%s|%s] bus count == %d, dropping properties for InputElement %d
[%s|%s] Invalid output channel layout, unable to initialize channel processors
[%p] invalid number of frames to process
%25s:%-5d Generated random string for temp file: %s
%s:%-5d Param value for %s not found in plist, using default value.
Setting DeviceStateB %u on %s
%s:%i failed to set blending graph delay parameter - %@
[%p] Successfully retrieved number of output channels (%u).
[%s|%s] Failed creating HOA decoders: format and input number of channels differ
%25s:%-5d Failed to set BeamFarfieldEQ data to SpectralProfile object. Invalid dictionary entry?
[%p] did initialize
%25s:%-5d SpatialProbabilityBase: Shape parameter min not set to (%f), it remains at the current value (%f). KappaMin should be in range [0, %f].\n
[%s|%s] APAC Metadata JSON:
%25s:%-5d CADSPUtility:%s:%d: VBAP Error; Unable to change speaker locations
%25s:%-5d ERROR: Failed accessing strings in GetParameterValueStrings.
%s: initialized %s
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve threshold.\"
%25s:%-5d Read plist key: %s
%25s:%-5d AUBeam2 Error: Invalid post eq data vector length from tuning file (expected %d bytes, actual %d bytes)
[%p] NeuralNet input size (%zu) not matching configured number of input channels (%u) times block size (%u).
[%s|%s] Initializing
%s:%-5d Format for Output Element %u is Invalid.
%25s:%-5d Loading nCoefficients from topLevelDict.\n
media chat other audio ducking level %.2f, db: %.2f
%s:%i deferred graph creation completed successfully
[%s|%s] probably corrupted binary blob for exclusion zones
[%s|%s] ERROR: Could not create mixer output file (ExtAudioFileSetProperty with kExtAudioFileProperty_ClientDataFormat returned %d)
%25s:%-5d creating random compiled IR file: %s
[ECv6] DrainPendingIRs: pending mic count (%zu) != initialized mic count (%u); applying overlap only
[%p] StoreMusicCodeTuningInPlist returned error %d
%25s:%-5d Input sample numbers cannot go backward in time!
%25s:%-5d Orientation %u is larger than the maximum allowed value (%u)
%s:%-5d Signal index set by user : %u
[%s|%s] Could not find biquad %u
%25s:%-5d _vp: vptimefreqconverter::synthesize: not configured for synthesis
[%{public}.*s] zero frame count for source %u
[%s] Computed grid order: %u (time taken: %.2f ms)
%25s:%-5d Successfully retrieved waitFrames (%u).
[%s|%s] Failed to update HRIRAttributes for divergence spatializers
%25s:%-5d AUECMicRef: ********* Logging ends *********\n
[%s|%s] ERROR: ImmersiveRendererData_V2: Inconsistent workflow: IRD version %u ≠ 2
Registering CMDeviceState device orientation observer %s
[%s|%s] The number of output buffer lists is not 1 (%u)
%25s:%-5d Loaded implementation from NeuralNetCache for model at %s.
%25s:%-5d AUECMIMO: Set classic mode.\n
%25s:%-5d Successfully loaded \"%s\"
%25s:%-5d Successfully retrieved activation function (%s) for Layer %zu.
[%p] \n Kernel Plist: Sample rate %5.3f
[%s|%s] Failed to create capture directory: %@
[%s|%s] Can't find a parameter value for parameter = %u, element = %u
%25s:%-5d Input size of SpatialProbabilityInputCDR_CF is not equal to the expected size (prop id: %u).\n
failed to set spatial metadata with status %u
[%s|%s] No renderer metadata config present
%25s:%-5d The ranged beam selection optimization requires that the channels are in order, but vLast = %i and vSecondLast = %i
%25s:%-5d Missing vector RowIndices\n
[%s|%s] ERROR: diffuse does not support interleaved output formats
%25s:%-5d AUECMIMO: ERLE measure in [dB] for mic-channel %u , internal: %f (dB), external: %f (dB)\n
%25s:%-5d NeuralNetVAD: Loading BlockSize from topLevelDict.
%25s:%-5d Ch %d, IV only AdaptiveDisplacement not supported, defaulting to Open Loop
[%s|%s] Can't set APAC property: ASC #%u referenced for group #%u but no input element exists for it
Failed to set AUSpatialMixer input stream format
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary OutputVectorDescriptor.\"
[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] is not a dict; skipping
[%p] Initialize finished with assumed bits %u \n
uplink speech mixer sample rate must be greater than zero
%25s:%-5d Setting property DATA (prop id: %d).
%25s:%-5d Failed to extract reverb tail vector from the dictionary entry keyed: '%s'
[%s|%s] Cleaning up AUSM
%25s:%-5d Successfully parsed the power smoothing time constants: %s
[%s|%s] Could not clear reverb blend on sc #%u, input element #%u, err = %d
[%s|%s] error %d while initializing NFC processor
%25s:%-5d %s
[%s] Computed grid weights, since they were not provided in the .ir file.
AUNeuralNet produced non finite output for input level %f dB. Resetting model state and output buffers. Will copy input channel 1 to all output channels and set ones for the mask.
[%p] will construct with M=%u, K=%u, delta=%f
%s: error %d uninitializing %s
%25s:%-5d Implementation cache enabled.
%25s:%-5d EXCEPTION (%d) [inputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve InputName.\"
%25s:%-5d Error loading ImagCoefficients.\n
%25s:%-5d Synchronization failure! One time series has outpaced the others: timeSeriesNo %i, synchSampleTime %u, GetSampleTime(eventNo, timeSeriesNo) = %u
%25s:%-5d Input size of SpatialProbabilityInputSteeringVector is not equal to the expected size (prop id: %u).\n
[%{public}.*s] uninitializing
[%s|%s] Triangle lookup failed for coordinates %f, %f, %f
%25s:%-5d EXCEPTION (%d) [biasDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Bias from dictionary Weights.\"
[ECv6] DrainPendingIRs: mic=%u per-channel length mismatch: pending=%zu, initialized=%zu; rejecting import
[%s|%s] Found SoundStages in Dictionary, but failed to set parameters on SoundStageManager
[%s|%s] Cleanup
[%p] audio captures are disabled
%25s:%-5d Invalid treble EQ sizes: Anchor gains size = %lu, # BQs = %lu\n
%25s:%-5d Camera direction %u is larger than the maximum allowed value (%u)
%25s:%-5d Safe limit offset = %f, should be negative. Setting to 0.
[%s|%s] Error %d setting Gain on group %u
AUDSPGraph Initialize() failed with exit code %d
[%s|%s] Could not load neural transcoder
%25s:%-5d Failed to queue staged kernel\n
%25s:%-5d NeuralNetEspressoV2 Destructing.
%25s:%-5d NeuralNetRES: Loading ECoutScale from topLevelDict.
[%s|setProperty] (scope=%u, element=%u): %s internal error: setter not implemented
%25s:%-5d Input size of SpatialProbabilityInputSubbandDOA_CF is not equal to the expected size (prop id: %u).\n
%25s:%-5d Successfully retrieved WaitFrames (%u).\n
%s:%-5d Invalid number (%u) of input buses requested. We only support 1-2 input buses.
%25s:%-5d kAUEndpointVAD3Property_EndpointerNonspeechDetectionEvent cannot be directly accessed.
[%p] Successfully retrieved number of input channels %u.
%25s:%-5d Missing dictionary NeuralNetImplementationType, set mImplType to default value.
[Room Congruence] %s: The input room volume must be greater than 0. Returning empty optional.
[%p] output format for bus %u: %s
[%s|setProperty] (scope=%u, element=%u): %s value out of range
%25s:%-5d mBypass: %u\n
[%p] Error[%d] pulling input from bus 0
[%s|%s] Error %u in setting property %u = %u for element %u
%25s:%-5d DirectionalModelType not found, being set to (%d).\n
%25s:%-5d AUNeuralNetVAD: Resetting state variables. Cleanup() started.\n
%25s:%-5d Successfully parsed the EnableCPMSClosedLoopControl param: [ %s ]
%25s:%-5d Could not load NeuralNetNS plist, exception (%d).\n
%s:%i input and output formats must match
%25s:%-5d The number of channels in the output format (%u) is larger than the number of uplink/selection beams (%u).\n
%25s:%-5d Input size of DenoiseInputSteeringVector is not equal to the expected size (prop id: %u).\n
%25s:%-5d AUSpeakerProtectionV3::SetProperty - Bypass %s->%s\n
%25s:%-5d Cannot get NumChannels Key
[%s|%s] ImmersiveRendererData could not set the spatialization algorithm for input %u, err = %d
%25s:%-5d AUBeam2 Error: Converting mic spacing from tuning file
%25s:%-5d Initialize Beam2N object with: sample rate = %f, transform size = %d, frame size = %d, number of beams = %d
%25s:%-5d AUBeamNF: Error: Beam object not initialized, won't dump diffraction filter
[%p] SNR: %f, Noise SPL: %f, Speech Probability Boolean: %f, Speech Probability Float: %f
%25s:%-5d AUNeuralNetSPP: Cleanup().\n
%s: Snap Coordinates initialized with ACL tag %u
%25s:%-5d SpatialProbabilityBase: Prior probabilities not set. Source prior (%f) should be in range [0, 1].\n
[%p] number of voice output buffers %u is not equal to expected number of voice output channels %u
%25s:%-5d Use '.ir' format
%25s:%-5d *** BIG PROBLEM ***: SpTS data should be present on this device, but we failed to fetch it. Failing back to open-loop.\n
[Room Congruence] %s: IRData User Data invalid - underlying CF object is nil.
[Room Congruence] %s invalid - %s values must be float.
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary Bias.\"
%s:%i update local parameter state after initializing the processing graph
[%s] Operating in 2D/horizontal-only mode
[%s] Failed to unlock memory
%25s:%-5d Updating stream formats
%25s:%-5d Error while resetting the graph: %@
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve ECoutScale.\"
[%p] The CFDictionaryRef passed to SetProperty is null.
%25s:%-5d Gap detected in the input time series. Filling in zeros.
[%p] AU's block size %s not matching the NeuralNet's block size %u. Will use a reblocker
%25s:%-5d  Input volume curve cannot be null
[%s|%s] (InputSignals) is NOT finite: (%d)
%25s:%-5d Cleanup.\n
VAD LPC order %d is larger than %d
%25s:%-5d Missing vector Coefficients.\n
%25s:%-5d AUBeamNF::~AUBeamNF (%p)
%25s:%-5d Successfully cached compiled IR file using secondary method: %s
%25s:%-5d Analysis period %f is not integer multiple of sine period
[%s|%s] EABL ingestion: err #%d while pulling the input
[%s|%s] Unsupported AuSMProcIndex %u on sc #%u, input element #%u
[%s|%s] Parsing SoundStage %@ dictionary
%s:%i invalid zoom curve value for dominance zoom
%25s:%-5d \tAUBeamNF: input stream format: %s
%25s:%-5d Could not queue staged kernel!\n
%25s:%-5d Successfully retrieved CombinedProbabilityMode (%g sec.).\n
%s was reset after initialize
[%{public}.*s] initializing (freqDomain=%d, data partitions=%zu, data channels=%zu, output channels=%zu, delay=%zu, xfade=%zu, applyDelay=%d)
%25s:%-5d EXCEPTION (%d) [inputDataType_ref.get_cf() == nullptr is false]: \"Missing dictionary DataType.\"
[%s|%s] Initializing with normalizedGain = %u
[%s] Assuming a grid order of 33.
[%p] Successfully default retrieved embedding mode (%g).
[%{public}.*s] reset
%25s:%-5d Plist has a bad render mode selection
%25s:%-5d Successfully retrieved beamforming filter length (%i).\n
%25s:%-5d Override missing SpCl Property with defaults clsp_srdc_r %f
%25s:%-5d Repair flag is true. Disable closed loop.
inInputBufferLists[%u]->mNumberBuffers=%u, ASBD::NumberChannelStreams(input.GetStreamFormat())=%u; kAudio_ParamError
[%s|%s] Invalid FFT size - must be power of 2
%25s:%-5d ChannelID key does not match channel order
[%{public}.*s] input coefficients span is null
[%{public}.*s] insufficient state storage for fractional delay lines: need %zu elements (offset %zu + %zu), got %zu
Failed to get Preference: '%s %s'. An exception was caught.
[%s|%s] Error %d setting divergence azimuth range to -1
[%{public}.*s] source(#%u): initialized at %uHz
[%s|%s] Could not set the stream format: invalid samplerate %f
%s:%-5d Could not retrieve fall back mic list. Will use default\n
%25s:%-5d Set TransducerCalibration property
[%s|%s] APAC flat metadata structure was not ready, late memory allocation in a RT context, to be fixed. ImmersiveRendererData: %s
Failed to set AUSpatialMixer output type
[%s|getProperty] (scope=%u, element=%u): %s called with nullptr for output data
%25s:%-5d AUDereverb: DRR measure in [dB] for mic-channel %u , internal: %f (dB), external: %f (dB)\n
%25s:%-5d kConvoyExpect5Streams is signalled; adding the Convoy PDM signal to the layout.
Failed to open austrip file, trying legacy location
GetProperty(UnitConverter): requested value (%.2fdB) is out of range [%.2f, %.2f]dB. Returning %.2f
[%p] Successfully retrieved number of input channels (%u).
%25s:%-5d Property data for unsupported property (%u) requested.
[%s|%s] Initializing.
%25s:%-5d Invalid number (%u) of input buses requested. We only support 1–3 buses.
%25s:%-5d Failed to retrieve beamforming filter length.\n
%25s:%-5d BeamSystemNoiseProfile dictionary not present in plist.
[%s|%s] Failed to set surround EQ filters
%25s:%-5d EXCEPTION (%d) [outputDescDict_ref.get_cf() == nullptr is false]: \"Missing dictionary OutputVectorDescriptor.\"
[%p] override 'ModelNetPathBaseOverride' to \"%s\"
%25s:%-5d Read input and output state names.
%25s:%-5d Failed to retrieve the beam description.\n
%25s:%-5d kAUEndpointVAD3Property_RecurrentVADSpeechDetectionEvent cannot be directly accessed.
%25s:%-5d Missing dictionary ImagCoefficients.\n
%25s:%-5d CADSPUtility:%s:%d: HOA Error; Inconsistent azimuth/elevation size
[%p] Construct AU and Kernel
%25s:%-5d Successfully retrieved ECoutScale (%g).\n
[%p] output format has %d channels, which is more than the max number of (%d)
Shared ambisonics input buffer allocated with %u channels x %u frames
[%s|%s] Error setting upmixer input layout with error code %d
[%s|%s] Failed to compute the correction envelope exponential decay coefficient. Returning empty optional.
[%s|%s] MagLS filters were converted into an IRData object incorrectly
%25s:%-5d Successfully parsed the power smoothing '%s' time scale.
[%p] Bad Property Value for Speech Mask selection
[%s|%s] Inconsistent behaviour: there was already an output capture file! Disposing of it.
%25s:%-5d AUDenoise: ********* Logging begins *********\nAUDenoise: logging (period, timestamp): (%f, %f) (s)\n
%25s:%-5d Ch %d, Using closed loop parameters refTemp=%f, invTempCo=%f, RebRef=%f
Failed to set AUDSPGraph input stream format
%25s:%-5d Loading from activationDict.
%25s:%-5d Output format is %s
%25s:%-5d AUBeamNF: Error: Could not read diffraction filter file %s
%25s:%-5d Destructing.
AUNeuralNetVADV2 received non finite input. Zeroing out %lu samples
[%s|%s] Invalid or unhandled filter order
[%s|%s] Not enough DiffuseProcessors for this output layout!
%25s:%-5d Bad orientation string: '%s'
[%s|%s] HOA power saving mode order (%u) can not be greater or equal to input HOA order (%u)
%25s:%-5d AUBeamItTD: (BFMicOut, BFLeeOut, AllUplinkBeams, AllSelectionBeams) is NOT finite: (%u, %u, %u, %u)
%s: loaded preset %s
Failed to reset new music graph
%25s:%-5d Invalid orientation %u
Intermediate storage allocated with %u channels
[%s|%s] PPV2 loaded with %u inputs and %u outputs
[%s|%s] Properties with scope = %u and element = %u in the property dictionary are ignored with APAC.
%25s:%-5d AUChannelSpecificDelay instantiated
NeuralNetGetTemporaryDirectoryPath: TMPDIR not set and NSFileManager failed, falling back to /tmp
[%{public}.*s] cannot set BankMode to BothEars when initialized with only 1 coefficient channel. Defaulting to LeftEar
Reset.\n
%s:%i will try to initialize
%25s:%-5d Input ECOutSignals buffer expected with (%u) channels.
%25s:%-5d EXCEPTION (%d) [activationDict_ref.get_cf() == nullptr is false]: \"Missing dictionary Activation.\"
Warning: %s was passed a ramped parameter event but does not implement them. Ignoring.
[%s|%s] dispatched update for dynamic XTC filter generation #:
%25s:%-5d EXCEPTION (%d): \"Unknown implementation type (%s).\"
%25s:%-5d AUECSUMO: ********* Reset ends *********\n
%25s:%-5d BeamSystemNoiseProfile found in plist.
[%{public}.*s] LSBank::getFilterIndex(): input indices out of bounds
[%{public}.*s] init scratch buffer is not float-aligned (base=%p, offset=%zu)
%25s:%-5d Saving plist and properties to AU preset
[%s|%s] Initialized in %.2fms with expected latency (samples) = %u
[%s|%s] failed to set tuning warper parameters
%25s:%-5d LoudnessCompensationEQEnable defaults-preferences is enabled: %s
%s:%i cannot process with DSP block size %u
%25s:%-5d Failed to retrieve '%@'
[%p] failed to interpret DSP graph file - %@
%s:%-5d Format for ECLee Input Element %u is Invalid.
%25s:%-5d Telemetry bus layout: [ %s ]
%s:%i unsupported normalization %i
[%s|%s] Error creating neural network - Neuralizer plist was not provided
%25s:%-5d AUBeam2: Error loading diffraction filter file at %s
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"MinInputChannelCount\"] has invalid value
%25s:%-5d Setting the stream format for the second input bus to match the format of the first bus.\n
%25s:%-5d Audio sampling rate must be 8000 Hz or higher.
[%s|%s] AUSM_VERBOSE|ReverbGrid #%u: %s
[%s|%s] Could not disable exclusion zone for input %u, err = %d
Preference '%s %s' retrieved as %s
[%s|%s] Channel processing dropped because the spatializer is locked
[%s|%s] ERROR: Could not create input capture file (ExtAudioFileCreateWithURL returned %d)
%25s:%-5d Invalid treble EQ sizes: BQ vectors must be same length\n
%25s:%-5d AUSpeakerProtectionV3::SetProperty - Telemetry data order. Set as: [ %s ]\n
Failed to set AUDSPGraph output stream format
[%p] failed to initialize - sample rates of FrontMic input bus and main output bus must be equal
[%p] No NeuralNets were loaded from plist.
%25s:%-5d EXCEPTION (%d) [outputName_ref.get_cf() == nullptr is false]: \"Failed to retrieve OutputName from (%s).\"
[%s|%s] Too many parameters for GlobalConfig
[%p] loading cached embedding
[%s|%s] invalid data size = %u for property = %u, expected %u
[%s|%s] Neural Transcoder network being loaded...
%25s:%-5d Initializing the directional model: azimuth (%f), elev (%f), model type (%d), shape parameter (%f).\n
%25s:%-5d Ch %d, Parameter updater could not be created. %s. defaulting to Open Loop
%25s:%-5d AUSpeakerProtectionV3::GetParameterInfo
%25s:%-5d Successfully parsed the EnableThermalControl param: [ %s ]
NeuralNetGetTemporaryDirectoryPath: using TMPDIR environment variable: %{public}s
[%s|%s] AUMonopoly does not support non-symmetric channel layouts as defined by channel labels
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"MCLPOutScale not loaded.\"
%25s:%-5d Internally set the forgetting factor for PSD as (%g).
%25s:%-5d Quantization not found, using default (%u) bit.\n
%25s:%-5d Number of microphones is not supported! Setting AU in Bypass mode.
[%{public}.*s] external state memory not provided, using internal allocation
[%s] Reporting %u samples of latency
%25s:%-5d Generating graph
[%s|%s] SetProperty called with kAudioUnitProperty_SpatialMixerHeadOrientationQuaternionXYZW while destruction is in progress
[%s|%s] The computed critical distance must be greater than 0. Returning empty optional.
%25s:%-5d MultiRadixRealFFT_Create() returned an error. Invalid block size?
[%p] \n Kernel Plist Bits Per Interval  : 
AUNeuralNet received non finite input. Zeroing out %lu samples
[%s|%s] No capture is configured. Not preparing the capture directory.
%25s:%-5d Loading LambdaPSD_TC from topLevelDict.
[%s|%s] (OutputSignals) is NOT finite: (%d)
[%s|%s] optional feature dictionary is being modified to ensure APAC features remain enabled.
[%{public}.*s] invalid parameters for ScratchStorageByteSize
[%p] Model bypassed: mBypass (%u) || !mSelectedValidModel (%d) || !selectedNeuralNet.model (%d)
[%s|%s] Inconsistent indexes for parameter = %u, element = %u
%s:%i Read param %i val %f from mDominanceZoom
[%s|%s] Failed to load HRIRs.
Buffers: EABL could not be created
%25s:%-5d Successfully Initialized.
AUECRMGS: Successfully initialized.\n
%25s:%-5d AUBeam2: Error loading post EQ file at %s
%s:%i Time Constant (seconds) set to: %f
[%p] Input size of EmbeddingVector (%lu) is not equal to the the expected size  (%lu) or (%lu) is not equal to (%lu).
%s: Crossover can not be applied if the number of drivers is < 2
[%s|%s] Could not initialize IR processor
Failed to set parameters on new music graph
%25s:%-5d Destructed.
%25s:%-5d Orientation locked after waiting for IO thread
[%s|%s] missing HRIR definition
[%s|%s] Error creating neural network - failure loading neural plist
[%p] input not connected
[%s|%s] Uninitialized
%s:%i failed to get processing graph neural net latency
%25s:%-5d Successfully retrieved Quantization (%u).\n
[%p] number of media input buffers %u is not equal to expected number of media input channels %u
AUSiriECGate:ProcessMultipleBufferLists error  - expected block size of %u but got %u instead
%s:%-5d Number of Output Elements provided is less than the Minimum required.
%s: Invalid format: %s
%25s:%-5d Retrieved info for property %u (%s)
[%{public}.*s] silent output period ends. Input had been silent for %f s
%25s:%-5d Successfully retrieved sample rate (%iHz).
%25s:%-5d CLSPKernel_v5::CLSPKernel_v5
[%s|%s] ImmersiveRendererData_V1 ingestion has begun
%25s:%-5d EXCEPTION (%d) [layerType_ref.get_cf() == nullptr is false]: \"Failed to retrieve layer type (Type) from dictionary LayerDescriptor.\"
[%p] \n Kernel Plist al  : 
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Failed to retrieve NumContextFrames.\"
[%p] Found model named (%s)...
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"WaitFrames not loaded.\"
%25s:%-5d Create SV-based estimator (SV dictionary)\n
AUTeakaLeakIR can not find an appropriate FFT Size, going into bypass
set CoreAudio reporter time period - %f
Failed to open propstrip file, trying legacy location
%s:%i neural net latency %f does not match denoise delay latency %f
[%{public}.*s] FFT failed for partition %zu, channel %zu
[%{public}.*s] insufficient state storage for TD convolver: need %zu elements, got %zu
AUSMScopeDynamic::%s: Cannot reduce number of Elements (%u -> %u) after initialization.
[ECv6_CPU] cycles=%llu instructions=%llu ns=%llu
[%p] Successfully retrieved number of output channels %u.
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Gains\"][%u][\"Output\"] has invalid value
%s:%i NeuralNetPlistPathOverride is set to null and thus removed
%25s:%-5d mVADinAudioOutputMode not found, being set to (%u).\n
%25s:%-5d  CAMutex::Lock: Could not lock the mutex
[%s|%s] Number of channels %u in requested audio channel layout %s is different than in the stream format.
%s:%i DereverbPresetPath is overriden to %s
%s:%i failed to create processing graph - %@
[%p] input format has %d channels, which is more than the max number of (%d)
[%s|%s] Custom Bypass Matrix was not found for input channel label = %u
%25s:%-5d NeuralNetVAD: Loading DirectionalModelConditionalTargetPrior from topLevelDict.
%25s:%-5d kAUEndpointVAD2Property_EventHandler is write-only.
[%{public}.*s] transformed directly into external span (%zu elements, zero-copy)
[%p] Failed to retrieve batch size, set to be (%u).
%25s:%-5d Successfully retrieved DirectionalModelConditionalTargetPrior (%g).\n
[%s] Constructing (ID %p)
Failed to parse default mode metadata
%25s:%-5d AUBeam2::ApplyParameterValues (%p)
AUEchoCancelerV6::InitializeEC: mic %u init params differ from mic 0 — refChannelsToUse %d/%d multiChanECMode %d/%d blockSize %u/%u filterSize %u/%u ecInitConvergence %u/%u enableFast %u/%u
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"MinOutputChannelCount\"] has invalid value
%25s:%-5d Number of subbbands in the externalShapeParameterPerFrequency (%d) does not match the actual number of subbands (%d). Setting the AU in bypass mode.
[%s|%s] Room configuration dictionary structurally invalid. Returning %s.
%25s:%-5d Initializing with Volume level: %s
%25s:%-5d AUBeam2::SetParameter (%p): id = %d, scope=%d, element=%d, inValue = %f
%25s:%-5d AudioUnitSetProperty failed for %s
[%p] Successfully retrieved embedding size (%g).
[%p] Initializing with configuration:\nGraph: %s \nAustrip: %s \nPropstrip: %s \nPropstrip resource path: %s
%25s:%-5d forgetting factor Lambda_TC not found, being set to (%g).\n
ERLE of mic %d: %f dB. Resulting Mic Gain: %f dB, ECLEE Gain: %f dB
%25s:%-5d Speaker telemetry data order not provided from property; assuming the default layout.
Failed to set Music EQ Ambience dictionary
NoiseGate registered successfully
%25s:%-5d Initializing.
[%s|%s] Setting high crossover, inFC = %f, inOrder = %u
[%p] input format is not valid
[%s|%s] Setting input bus count = %u (not changed)
[%s|%s] Clearing early reflections HOA IR
[%s|%s] %s: Invalid MatrixMix Output Type
%25s:%-5d Invoking BNNSGraphContextMake
[%s|%s] ImmersiveRendererData failed to set the rendering flags for input %u, err = %d
Media Chat: setting other audio ducking level %.2f
%25s:%-5d Write-only property LockOrientation was read?
[%p] SetPlistValuesToInternalKernelVariables returned error %u
[%s|%s] Loading preset: %s
%25s:%-5d Successfully retrieved output name (%s).
%25s:%-5d Construct NeuralNetEspressoV2.
%25s:%-5d Speaker gain-link grouping not set; using default (all in group 0).
[%s|%s] Could not set source pitch on sc #%u, input element #%u
Failed to open new music austrip file
[%p] Loading default embedding mode from plist.
%25s:%-5d Failed to create frequency smoothing matrix!
%25s:%-5d Volume Input/Mapped: %f, %f
%25s:%-5d Start reading NeuralNetVAD parameters.
At least one input bus, bus1, is need. It is a required input\n
%25s:%-5d CPMS file logging is enabled.
%25s:%-5d Failed to load noise estimate post-processor. Most likely wrong sample rate:%d. Will be bypassed
[%s|%s] Control Points found to be coplanar. Unable to compute triangulation.
[%p] \n Kernel Plist: gamma %5.3f
[%s|%s] Failed to set low crossover LPF coefficients
[%s|%s] Setting late reverb bus count = %u
%25s:%-5d Create SV-based estimator (external SV)\n
[%{public}.*s] source(#%u) destroyed
%25s:%-5d Initialize Beam object with: sample rate = %f, optimal frame size = %d, number of beams = %d
[%p] failed to locate graph file - %s
%25s:%-5d Found the %s plist entry for channel %i.
%25s:%-5d AUBeamNF Error: Invalid diffraction filter data vector length from tuning file (expected %d bytes, actual %d bytes)
Unregistering UI orientation observer %s
AUAGCV2 VAD failed to create sample rate converter with status %s
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar DataBias from dictionary Weights.\"
%25s:%-5d Unlocking orientation
%25s:%-5d exception!
%25s:%-5d ComputeEngineName not found, using default.\n
%25s:%-5d Number of channel in the output stream (%u) not equal to the expected number of channels (%u).\n
%25s:%-5d Ch %d, Convoy calibration parameters not present
[%s|%s] Target latency %u is too small (upmixer latency=%u, native blocksize=%u)
history window blocks to average: %u
[%s|%s] cannot initialize with inNumOutputChannels = %d
[%s] Configured filterbank with %u frequency bands
[%s|%s] invalid scope = %u for global scope property = %u
%25s:%-5d Volume Input Map: %s
%25s:%-5d Loading NumLayers from topLevelDict.
[%{public}.*s] source (inactive) was already initialized with different settings, will reinitialize processors
[%s|%s] Room configuration logically invalid. Returning %s.
Error AUMicBlend::loadMask: %s\n
[%s|%s] Metadata parsing error: %s
%25s:%-5d Reported latency not supplied for box %s
[%p] number of voice input buffers %u is not equal to expected number of voice input channels %u
[%s|%s] Failed to set audio channel layout %s. Current audio channel layout tag = %s
%25s:%-5d AUECSUMO: ********* Logging begins *********\nAUECSUMO: logging (period, timestamp): (%f, %f) (s)\nAUECSUMO: state variables have finite values (1 if True): %u\nAUECSUMO: ref-signal buffers have finite values (1 if True): %u\nAUEC
%25s:%-5d Use '.mil' format
[%s|%s] EABL ingestion: Invalid buffer list or invalid number of buffers lists
[%s|%s] Too many blocks
%25s:%-5d Successfully retrieved Microphone Sensitivity/Hearing Threshold (%d) dB.\n
%25s:%-5d Update index size is too small.
%25s:%-5d Process called without a graph!
[%s] Unsupported kAUParametricProcessorV2Property_HopSize (must be either 64 or 128)
[%s|%s] Target latency %u is not a multiple of native blocksize (upmixer latency=%u, native blocksize=%u)
%s: Filter matrix size inconsistent with user-defined filter length; IR file may not render
[%s|%s] Invalid number of output channels %u
[%{public}.*s] setting up late reverb processor (shared instance)
CMDeviceStateManager not available
Failed to set austrip on AUDSPGraph
AUECRMDF::ProcessMultipleBufferLists error - wrong (%u) block size expected (%u)\n
%25s:%-5d app sandboxed: file cache not possible
%s: factory preset #%d not defined
%25s:%-5d successful reset.\n
%25s:%-5d Successfully retrieved Type (%s) for LayerDescriptor %zu.
%25s:%-5d ->%s %p
Use processing graph latency as an estimate of the tail time
%25s:%-5d  Output volume curve is not monotonic. %s
%25s:%-5d (OutputSignals) is NOT finite: (%u)\n
%25s:%-5d AUDereverb: (InputSignals, EchoEstimates) is NOT finite: (%u, %u)\n
%25s:%-5d doSecondaryCacheIRFile fallback: compile using default output path
%25s:%-5d AUBeam2 Error: Invalid diffraction filter data vector length from tuning file (expected %d bytes, actual %d bytes)
%25s:%-5d AUBeam2: Error: Number of unique bands is zero, won't dump diffraction filter
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"KalmanObservationStd not loaded.\"
[%s|%s] Could not set source yaw on sc #%u, input element #%u
[%p] initialize mask related variables
%s: error %d setting preset on %s
%25s:%-5d Target elevation not set to (%f), it remains at the current value (%f). Elevation must be in range [-90, 90].\n
%25s:%-5d Preparing MIL2BNNS_PREPROCESSED NeuralNet implementation.
%25s:%-5d AUBeamNF: Error no diffraction filter data
[%s|%s] Failed to compute upper RT60 limit.
%s:%i Setting manual zoom amount %f on mDominanceZoom
%25s:%-5d Loading from outputDescDict.
%25s:%-5d ERROR: Failed to dispose of internal AU.
[%p] Loading embedding size from plist.
%25s:%-5d Successfully retrieved mOutputMaskMode (%u).\n
Could not load built-in speaker preset file: invalid model/product name!
%25s:%-5d Loading from weightsDict.
[ECv6] SetProperty(InitializeIR) rejected: value is not a CFDictionaryRef
ioData.mNumberBuffers=%u, ASBD::NumberChannelStreams(output.GetStreamFormat())=%u; kAudio_ParamError
%s:%i BypassEffectWithLatency state unchanged: %d
[%s|%s] Trying to render while uninitialized
[%s|%s] Invalid Parameter ID: %u
%25s:%-5d AUBeamNF: Error no post EQ data
[%s|%s] updating dynamic XTC filters:
%25s:%-5d Unknown error thrown\n
[%{public}.*s] partition %zu, channel %zu is fully zero-padded (past input end)
ioData.mNumberBuffers=%u, ASBD::NumberChannelStreams(input.GetStreamFormat())=%u; kAudio_ParamError
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"MaxOutputChannelCount\"] has invalid value
%s:%i constructed
%25s:%-5d Cross-fade Triggered: mBypassCounter: %u\n
%25s:%-5d AUECMIMO: Using logPeriod of (%g)s as specified in defaults write ecmimo_log_period_in_seconds.\n
%25s:%-5d AUECMIMO: Reset.\n
%25s:%-5d Input kappaMin must be lower than kappaMax. Skipping updating model with CDR-based frequency dependent shape parameter.\n
%25s:%-5d Setting property EnableSubbandDOACalculation failed (prop id: %d). *inData should be UInt32. Provided inDataSize = %u.\n
Channel number mismatch (mic = %u, eclee = %u, out = %u)
[%s|%s] error %d setting output scope property %u on %s
%25s:%-5d AUDenoise: SNR measure in [dB] for mic-channel %u , internal: %f (dB), external: %f (dB)\n
%25s:%-5d EXCEPTION (%d): \"Unknown streaming mode (%d).\"
%25s:%-5d Could not fully parse the power gain limit. Will use the default
uplink speech mixer failed to interpret \"%@\" - %@
[%s|%s] Could not set binaural compatibility mode on sc #%u, input element #%u
%25s:%-5d \tAUBeam2: output stream format: %s
%25s:%-5d _vp: vptimefreqconverter::analyze: not configured for conversion
[%p] failed to set bypass property; size error; inDataSize[%u]
%s| Reconfiguring non-existent SharedIRBus channel %u. Total number of channels = %u
AUECRMGS: Initialize.\n
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"Missing scalar Size from dictionary OutputVectorDescriptor.\"
%25s:%-5d CADSPUtility:%s:%d: Delaunay Triangulation Error: Convex hull could not be created. Check for overlapping speakers. 
%s:%i failed to set bypass graph delay parameter
%s: ERROR: Filters NOT Updated to IR Data object
[%s|%s] Could not set default channel layout after number of channels in a stream changed to %u: error = %d
[%p]  AuxCodeUseInInt %u 
[%s|%s] Invalid channel label in the preset, some channel parameters are probably ignored.
%25s:%-5d InputSignals cannot be NULL. It is a required input.\n
%25s:%-5d This instance is ideally open-loop; setting up the open-loop ThermalStateVector_v3.
AUECRMGS::ProcessMultipleBufferLists error - wrong (%u) block size expected (%u)\n
%25s:%-5d EXCEPTION (%d): \"Unknown quantization type (%u).\"
%s:%i bad outMatrix num rows
[%s|%s] updating early room for input %d
[%s|%s] No headphone factory preset was set.
[%s|%s] Error scheduling unsupported parameter (ramped) #%u: param = %u, scope = %u, element = %u
[%s|%s] Invalid Parameter Info
AUECRMGS: ********* Reset begins *********\nAUECRMGS: ref-signal buffers have finite values (1 if True): %u\nAUECRMGS: EC output buffers have valid values (1 if True): %u\n
%25s:%-5d AUBeam2::Initialize (%p)
%25s:%-5d Loading SampleRate from topLevelDict.
%25s:%-5d InputSignal cannot be NULL. It is a required input\n
[%s|%s] ERROR: Could not create input capture file (ExtAudioFileSetProperty with kExtAudioFileProperty_ClientDataFormat returned %d; format was %s)
%25s:%-5d AUBeam2::DumpPostEQ (%p)
[%s|%s] Setting output stream format: %s
%25s:%-5d AUECMicRef: ********* Reset ends *********\n
Media Chat: setting ducking ramp time %.2fs
%s:%i allocate temporary ABL
%s: AUXTC file loaded: %s
%25s:%-5d Number of subbbands in the plist (%d) does not match the actual number of subbands (%d). Setting the AU in bypass mode.
%25s:%-5d AUECSUMO: Successfully initialized.\n
%25s:%-5d MIL2BNNS extension is '%s'
[%s|%s] AUSM_VERBOSE|CombinedReverbIRWeights[%u]={%s}
%25s:%-5d Error in SetSNREstimator(): %s (%s)\n
%25s:%-5d Successfully computed SparseMatrix * Ones data (%g) at index (%u).\n
%25s:%-5d %s camera FOV (%u): %f
[%p] Creating NeuralNet model (%d)
[%s|%s] AUSM_VERBOSE: %s
%25s:%-5d Override missing SpCl Property with defaults clsp_srdc %f
[%s|%s] EABL ingestion: mdFrameHeader: frameStartTime = %f, frameDuration = %f, trimmedSamplesFromBeginning = %u, trimmedSamplesFromEnd = %u, type = %u, reserved1 = %u, intermediateCountToFull = %u, headerSize = %u, eventCount = %u
%25s:%-5d Failed to retrieve Microphone Sensitivity/Hearing Threshold !\n
%25s:%-5d Invalid bass EQ sizes: Anchor gains size = %lu, # BQs = %lu\n
%25s:%-5d AUSpeakerProtectionV3::SetParameter(%d): %f -> %f\n
[%s|%s] Unknown proprietaryStaticData param index %u on sc #%u, input element #%u
[%s|%s] Input Element #%u referenced for objectID #%u does not exist
%25s:%-5d AUBase::SaveState didn't produce valid dictionary?
%25s:%-5d Orientation locked timed out! Is IO running?
[%s|%s] Error %d while fetching the parameter info canRamp: param = %u, scope = %u, element = %u
[%s|%s] Uninitializing ScottyLite
%s:%-5d Invalid number (%u) of input buses requested. We only support 1 bus.
%25s:%-5d Successfully retrieved NumLayers (%u).\n
[%{public}.*s] constructed %lu-bit processor (external/internal) = (%uHz/%uHz), delay mode %u
At least one output bus, bus1, is need. It is a required output\n
%25s:%-5d Successfully retrieved BlockSize (%u).\n
[%s|%s] ERROR: no capture dir path available
%25s:%-5d Ch %d, Set up for ConvoyAdaptiveDisplacement
%25s:%-5d Successfully parsed the system plist params.
[%s|%s] %u channel parameters using default values
[%s|%s] Cannot use Crossover option due to no LFE in OutputACL --- reverting to Standard
%25s:%-5d Initialize called without setting setting NeuralNetNSLayers or NeuralNetRESLayers plist! Setting AU in Bypass mode.\n
%s:%i initialize base
ToneMeister registered successfully
[%{public}.*s] TD coefficient size too small (need at least %zu samples for %zu partitions, got %zu)
%25s:%-5d Number of channel in the input stream (%u) not equal to the expected number of channels (%u).\n
%s:%i use %u I/O channels with %u channel DSP and batch size %u
[%s|%s] Failed creating HOA decoders for output channel layout tag = %u (%s); Distances for all drivers is zero. Defaulting to stereo
Registering device orientation observer %s
%25s:%-5d Creating log Hann matrix mNumFreqBins=%u frequencySmoothing=%f
%25s:%-5d Adapt orientation set to %i
%25s:%-5d EXCEPTION (%d) [mInputSize != featureVectorSize is false]: \"mInputSize of NeuralNet (%u) is not matching the feature vector size (%u).\"
Render
[%s] BlockSize (%u) is not divisible by HopSize (%u). Running in passthrough mode.
Failed to create propstrip plist
%25s:%-5d Starting initialization.
%25s:%-5d Initialize\n
%25s:%-5d Getting property SubbandDOA_CF failed (prop id: %d).
%25s:%-5d Streaming mode CopyOutStateToInState: bind input and output states.
The inData passed to SetProperty is null.
[%p] AUReferenceSignal's property list \"Configurations\"[%u][\"Orientations\"][%u] has invalid value
[%s|%s] Creating a timer to check defaults writes while running
[%s|%s] PreMix load time = %.2f ms
%25s:%-5d Loading NumInputChannels from topLevelDict.
%25s:%-5d StreamingMode not found, using default.
%25s:%-5d Successfully retrieved SpatialSPPCutOff (%g).\n
[%s|%s] AUSM_VERBOSE|PostProcReverbIRWeights[%u]={%s}
%25s:%-5d Found the dictionary ImagCoefficients.\n
[%p] NeuralNet input size (%zu) exceeds freq domain format size: input channels (%u) num bins (%u) batch size (%u).
%25s:%-5d Successfully retrieved Kalman process std (%g).
%25s:%-5d Initialize called without setting setting NeuralNetRESLayers plist! Setting AU in Bypass mode.\n
CFProperty::%s: file %s not found
%25s:%-5d AUECMicRef: ********* Logging begins *********\nAUECMicRef: logging (period, timestamp): (%f, %f) (s)\nAUECMicRef: state variables have finite values (1 if True): %u\nAUECMicRef: ref-signal buffers have finite values (1 if True): 
%25s:%-5d This instance is ideally closed-loop; setting up the closed-loop ThermalStateVector_v3.
Failed to set new music propstrip on AUDSPGraph
%25s:%-5d Setting the default parameter values.
[%s|%s] Can not set OutOfPhase when AU is initialized
[%s|%s] NeuralNet initialization using plist failed with CAException %d: %s.
%25s:%-5d _vp: vptimefreqconverter::synthesize: not configured for conversion
%25s:%-5d Format check for scope %i element %i: %s. Valid: %i
%s:%i set CoreAudio reporter time period - %f
[%s|%s] setting factory preset #%u
[%s|%s] Could not initialize FDN
[%p] AU can only support one input bus but receives %d
SetProperty( kAudioUnitProperty_DspLibDictionary ) Error data\n
%25s:%-5d Setting property SetParameters
[%p] \n Kernel Plist: rampUp %5.3f
%25s:%-5d Successfully retrieved '%@' as %@
[%s|%s] Initializing STFTUpmixer
%25s:%-5d Successfully retrieved number of states (%d).
%25s:%-5d Successfully retrieved output state name (%s).
%25s:%-5d AUSpeakerProtectionV3::SetProperty - Thermal State Override %u->%u\n
[%s|%s] SourceExtentProcessor is not available, HOASpatializer will ignore source extent
[%p] Loading embedding mode from plist.
[%p] cleanup
[%p] failed to calculate expected graph output frame count - %@
%25s:%-5d Changed config plist successfully\n
[%s|%s] ImmersiveRendererData failed to set the rendering flags for input #%u, err = %d
[%{public}.*s] numPartitions must be specified for frequency-domain coefficients
%25s:%-5d Invalid state value!
%25s:%-5d ERROR: We have not been configured fully; we could not initialize the kernel and will process in soft bypass.
%s:%i NeuralNetPlistPath is overriden to %s
%s %s: aufx %s appl only supports render method; processing will be bypassed
%25s:%-5d rebv=%f, reb20=%f desiredwin=%f, thermalsampleperiod=%d, tau=%f, cnt=%d, f_a_des=%f, f_a=%f, fs=%f
VAD sparsity length %f ms is larger than %f
[%s|%s] Invalid number of channels %u
%25s:%-5d EXCEPTION (%d) [inputDescDict_ref.get_cf() == nullptr is false]: \"Missing dictionary InputVectorDescriptor.\"
[%s|%s] ERROR, cannot process with %d output channels
[%s|%s] AUMonopoly does not support multiple LFEs - Duplicate LFE label
[%p] setting DSP graph parameter %u to value %f
[%s|%s] ImmersiveRendererData: receiving %u bytes
[%s|%s] Could not reset directivity index for group #%u: err = %d
Failed to set Spatial dictionary
[%p] Could not load metadata using the plist, unknown exception.
[%s|%s] Switching from Render to ProcessMultiple without reinitializing
%25s:%-5d End Initialize()
cannot migrate AudioUnit assets for current process
[%s|%s] Error creating neural network - input tag is not FOA/HOA
%25s:%-5d No reverb tail has been specified for this sample rate (%gHz). AU going into soft bypass mode.
[ECv6] LoadPendingIRsFromDictionary: missing or non-array \"IRs\" key
[%s|%s] Frame size %u is not half of FFT size %u
[%s] Loading ATFs: %s
%25s:%-5d ----
[%s|%s] Resetting post-processing reverb
[%s|%s] Initializing auto mode reverb
[%s|%s] Invalid output type %u when trying to initialize with kSpatializationAlgorithm_UseOutputType; reverting to external speakers
%25s:%-5d ECOutSignals cannot be NULL. It is a required input.
%25s:%-5d Threw an unknown exception\n
%25s:%-5d Loading from biasDict.
%25s:%-5d Plist path given as %s by defaults write value
[%p] mNeuralNet output size: %lu
[%p] NeuralNet output size (%zu) not matching configured number of output channels (%u) times block size (%u) times batch size (%u).
[%s|%s] Parameter event type unknown (%u)
[%{public}.*s] settings have changed, reinitializing
[%p] initialize
[%s|%s] Invalid input scope element %u
%25s:%-5d mNumFadeFrames: %u\n
[%s|%s] ImmersiveRendererData: exported %zu bytes to %s
[%s|%s] Distance Attenuation: Unsupported attenuation law %u. Defaulting to 'realistic'
[%s|%s] Can not set ACLT when AU is initialized
%25s:%-5d _vp: gate: err %d initializing res fft to %d
[%s] Constructing
[%p] \n Kernel Plist: ChirpHzPerSec %5.3f
%s:%i initialization duration %lld ms
[%s|%s] Late IR is HOA: updating early reflections to use same IR file
%25s:%-5d Successfully parsed all %lu ClosedLoopParameters structures.
Telemetry provided, but CheckBuffer() failed: telemetry numBuffers=%u, numCh=%u, dataBytes=%u, inFramesToProcess=%u. Closed loop disabled.
%25s:%-5d EXCEPTION (%d) [err != noErr is false]: \"FFT2Mel matrix not loaded.\"
%25s:%-5d Filesystem (primary or secondary) cache unsuccessful, will save to NeuralNetCache on destruction.
%25s:%-5d Spatial capture graph source generation: bad sample rate provided: %f
[%s|%s] Could not set exclusion zone array on input %u, err = %d
%25s:%-5d Initializing with LUTSystem:\n%s
%s:%i bad dominanceValues size
%s:%i failed to create bypass graph model
[%p] Tried to select a mask indexed at (%u), but only (%u) masks are available
[%p] processed output format not supported
[%{public}.*s] scratch buffer too small for coefficient update
[%s|%s] No default channel layout for %u input channels
[%p] Failed to retrieve default embedding mode
[%p] Loading number of input channels from plist.
[%p] Searching plist for model named (%s)...
[%s|%s] invalid parameter id %d (input scope)
%25s:%-5d Empty temp path
[%s|%s] Failed to match the parameters. Returning empty optional.
[%s|%s] APAC metadata parsing: changing aclt for sc #%u to %u, input element #%u
%25s:%-5d This device uses SpTS for speaker calibration, but it has already been applied. Omitting another application.\n
[%s|%s] ERROR: ImmersiveRendererData_V2 struct too small
[%s|%s] Could not %s exclusion zone on input %u, err = %d
%25s:%-5d Bad channel selection array! count = %u
[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] (Mic=%u Ref=%u) Coefficients size mismatch: got %ld bytes, expected %zu; skipping
[%s|%s] ERROR: Could not create mixer output capture file (no capture dir path available)
%25s:%-5d Filesystem (primary or secondary) cache was successful, will not save to NeuralNetCache.
%25s:%-5d Missing TaskID, TaskIteration, BlockSize, or CacheIRFile in plist  --- can not generate cache file
Media Chat: setting dynamic ducking accumulation time %.2fs
softlink:r:path:/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit
RefSpecSpreadAtErp
DynamicBatchSize
HF normal level diff
Uniform
Rm0_max not found in inConfig
    Reference Distance: 
DualEC minHangTime
Float32
dst.mNumberChannels == src.mNumberChannels
Mic 1 EC LEE
ChannelID
CL
SensitivityControlLinkSpeakerTypeC
ConvoyDisplacementControllerV2
  Coordinates:  [
Meter 3 Correction Select
]                     \n    [def numOutputs 
(GW) Exponent for energy values for (X,Y) weighting
Built-In Speaker Media Playback
Re-Convergence + Rate Cal
Smoothing constant for error PSD
(IRW) Prominence level of a stream
Soft clipping
FEV Gain at Min. Volume
ParametricEncoder
Delay of QRD (output smoothing, only if filtLen > blockSize)
EnRatioGainOutEnFloor
SpTS key described 
Distance estimated at the current frame
result.size() == C.size()
Apple: AUOneChannelNS
room congruence tuning dictionary
En_Th
Thermal_AmbientTemp
mTmpVector3.size() >= length
MaskEnergy2
Current residual sparsity above smoothed background
Auto Volume High Noise
DirectionalTargetAzimuth
band 2: gain table stop
LKFS
TimeScales
(Glitchfull) Enable Low Delay Mode
|OutputElement
sppv3_closed_loop_enabled
PowerGroupHardLimit3
Gain: In %u Out %u
STFT center minimum gain
Auto Volume High Slope
UpdateTuningWarper
Low Pass Stop Frequency
AUVolumeTaper_ViewFactory
Current Gain
EQ0 - Quality
SoundGaindB Offset
Complement Watson
computeSpectralMatchingCorrectionBiquads
Acoustic ID: %@
 (linFullSignal 
CreateSharedCAReportingClient
Breakpoints
compressorLPF2_b1
AUDynamicDuckerLog
GetPosition
bss_bypass
unordered_map::at: key not found
speakerType A: Magnet: thermal time constant [s]
_timeout > 0
SetParameterImmediately
clsp_caltemp
RdcMinOhms
ConfigurationParameters
FIR Filter Group Delay In Percent Of Filter Size
NS: Noise suppression amount
 unsigned
normalize
AUSpatialProbability.cpp
Noise estimate smoothing time
WindowParams
Monitor
_snr
(unknown_instance_id)
RoomCoordinates
mKappaSubband.size() == (inDataByteSize / sizeof(Float32))
Filterbank
Type of recursive update of statistics for iPMWF
MaxAttenuationTop
focusedPatcher-sc.wav\"     focusedPatcher \n            record \"
Crossover frequency.
LsmFrameLog.bin
power_1000ms
/System/Library/Audio/Tunings
All Pass
plantTap_Q
RdcMaxOhms
AmplitudeLimit
\nTlimAdjCap = 
(T) Long (Full) convergence Time Interval (sec)
ImpedanceInvertPhase
Frequency EQ Enable
Min Omni Blend Crossover Frequency.
Raw Scale Smoothing
Combiner Short Win Max dbFS
SelectFrequencyResponseGraph
Apple: AUADAMSink
band 0: makeup gain
ZmsSetCoherenceToZeroThresholdDecibel_1st
(Real-Tunable/Optional) Total HI Asset length in seconds
buf[len - 1] != '0'
beam2_dump_diffr
RdcErrorThreshold
MultiplyVectorScalar
ERROR : opening 3D files...\n
Found the dictionary ImagCoefficients.
Enable Dual KF
D.size() == A.size()
thiele_small_kms
dynamic filter 13
Err_Data_ch
\nTempCo20 = 
Smoothing TC - Echo Level calculation.
createHOADecoders
Cutoff frequency for wind boost limiting.
PeakDispDecayTime
radiator_p1_imag
radiator_z1_real
DebugSoloInputElement
log.{}.{}.csv
critical voltage
tDSP_zvtzmmult
mModel->mObservationTransition[currentObservation].size() > mPreviousObservation
(I) Input to gate speex speech prob
mSmoothSuppressionGains.size() == mNumInputChannels
(Tun) Corrective Cut Cutoff
enable reverb send decorrelation filters
upwards compression range
pSrcCh < pSrc.getNumChannels()
PhaseFlip
ParameterCanRamp
Combining Related Parameters
Frequency for detection statistic of probability of occluded noisy microphone
LSLateProcessor.cpp
mModel->mObservationTransition.size() > currentObservation
AmpHiZWatermark_typeA
Use uniform diagonal elements to initilize covariance matrices
i != val.m_value.object->cend()
Normal
mclp_log_period_in_seconds
GainAttackTime
\n         box postGain (aufx dbgn abox) 1 1\n         ;\n         ; Linear spatial (full signal)\n         ;\n         
```
