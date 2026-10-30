# `AUAudioUnitXPCProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `_AURemoteParameterSynchronization`
- 0 instance variables, 0 properties, 39 instance methods, 0 class methods

## Instance methods

```
-[AUAudioUnitXPCProtocol reset:];
-[AUAudioUnitXPCProtocol close:];
-[AUAudioUnitXPCProtocol initialize:reply:];
-[AUAudioUnitXPCProtocol addPropertyObserver:context:reply:];
-[AUAudioUnitXPCProtocol cancelSpeechRequest:];
-[AUAudioUnitXPCProtocol createRenderPipe:formats:maxFrames:midiOutSizeHint:resources:reply:];
-[AUAudioUnitXPCProtocol deleteUserPreset:reply:];
-[AUAudioUnitXPCProtocol destroyRenderPipe:reply:];
-[AUAudioUnitXPCProtocol disableProfile:cable:onChannel:reply:];
-[AUAudioUnitXPCProtocol enableProfile:cable:onChannel:reply:];
-[AUAudioUnitXPCProtocol getBusses:reply:];
-[AUAudioUnitXPCProtocol getCustomMessageChannelFor:reply:];
-[AUAudioUnitXPCProtocol getParameter:sequenceNumber:reply:];
-[AUAudioUnitXPCProtocol getParameterTree:];
-[AUAudioUnitXPCProtocol getSpeechVoices:];
-[AUAudioUnitXPCProtocol loadUserPresets:];
-[AUAudioUnitXPCProtocol localCachingDisabled:newValue:reply:];
-[AUAudioUnitXPCProtocol open:instanceUUID:reply:];
-[AUAudioUnitXPCProtocol parameterNode:displayNameWithLength:reply:];
-[AUAudioUnitXPCProtocol parameterStringFromValue:currentValue:address:reply:];
-[AUAudioUnitXPCProtocol parameterValueFromString:address:reply:];
-[AUAudioUnitXPCProtocol parametersForOverviewWithCount:reply:];
-[AUAudioUnitXPCProtocol presetStateFor:reply:];
-[AUAudioUnitXPCProtocol profileStateForCable:channel:reply:];
-[AUAudioUnitXPCProtocol removePropertyObserver:context:reply:];
-[AUAudioUnitXPCProtocol retrieveInstanceUUID:];
-[AUAudioUnitXPCProtocol saveUserPreset:state:reply:];
-[AUAudioUnitXPCProtocol selectViewConfiguration:reply:];
-[AUAudioUnitXPCProtocol setBusCount:scope:reply:];
-[AUAudioUnitXPCProtocol setBusFormat:scope:format:reply:];
-[AUAudioUnitXPCProtocol setValue:forKey:reply:];
-[AUAudioUnitXPCProtocol setValue:forProperty:propagateError:reply:];
-[AUAudioUnitXPCProtocol supportedViewConfigurations:reply:];
-[AUAudioUnitXPCProtocol synthesizeSpeechRequest:reply:];
-[AUAudioUnitXPCProtocol uninitialize:];
-[AUAudioUnitXPCProtocol updateHostCallbacks:reply:];
-[AUAudioUnitXPCProtocol updateWorkgroupMirror:reply:];
-[AUAudioUnitXPCProtocol valueForKey:reply:];
-[AUAudioUnitXPCProtocol valueForProperty:propagateError:reply:];
```
