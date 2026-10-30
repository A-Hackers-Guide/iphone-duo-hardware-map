# `AUAudioUnitV2Bridge`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnit`
- 15 instance variables, 1 properties, 43 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _eventListenerQueue;
^{AUListenerBase=} _eventListener;
^{AUListenerBase=} _parameterListener;
B _removingObserverWithContext;
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _willSetFullState;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _eventsTriggeringParameterTreeInvalidation;
@"NSObject<OS_dispatch_queue>" _parameterTreeRebuildQueue;
^{OpaqueAudioComponentInstance=} _audioUnit;
B _audioUnitIsOwned;
@"AUV2BridgeBusArray" _inputBusses;
@"AUV2BridgeBusArray" _outputBusses;
@"AUParameterTree" _cachedParameterTree;
{unique_ptr<AUAudioUnitV2Bridge_Renderer, std::default_delete<AUAudioUnitV2Bridge_Renderer>>=""{?="__ptr_"^{AUAudioUnitV2Bridge_Renderer}}} _renderer;
@? _MIDIOutputEventBlock;
@? _MIDIOutputEventListBlock;
```

## Properties

```
@property (T^{OpaqueAudioComponentInstance=},R,N) audioUnit;
```

## Class methods

```
+[AUAudioUnitV2Bridge automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[AUAudioUnitV2Bridge addObserver:forKeyPath:options:context:];
-[AUAudioUnitV2Bridge removeObserver:forKeyPath:];
-[AUAudioUnitV2Bridge requestViewControllerWithCompletionHandler:];
-[AUAudioUnitV2Bridge setCurrentPreset:];
-[AUAudioUnitV2Bridge initWithComponentDescription:options:error:];
-[AUAudioUnitV2Bridge dealloc];
-[AUAudioUnitV2Bridge reset];
-[AUAudioUnitV2Bridge initWithAudioUnit:description:];
-[AUAudioUnitV2Bridge removeObserver:forKeyPath:context:];
-[AUAudioUnitV2Bridge enableBus:scope:enable:];
-[AUAudioUnitV2Bridge MIDIOutputEventListBlock];
-[AUAudioUnitV2Bridge _rebuildBusses:];
-[AUAudioUnitV2Bridge parametersForOverviewWithCount:];
-[AUAudioUnitV2Bridge MIDIOutputEventBlock];
-[AUAudioUnitV2Bridge _buildNewParameterTree];
-[AUAudioUnitV2Bridge _createEventListenerQueue];
-[AUAudioUnitV2Bridge _createParameterTree];
-[AUAudioUnitV2Bridge _elementCount:];
-[AUAudioUnitV2Bridge _elementCountWritable:];
-[AUAudioUnitV2Bridge _invalidateParameterTree:];
-[AUAudioUnitV2Bridge _notifyParameterChange:];
-[AUAudioUnitV2Bridge _setElementCount:count:error:];
-[AUAudioUnitV2Bridge _setValue:forKey:error:];
-[AUAudioUnitV2Bridge _valueForProperty:error:];
-[AUAudioUnitV2Bridge allocateRenderResourcesAndReturnError:];
-[AUAudioUnitV2Bridge audioUnit];
-[AUAudioUnitV2Bridge channelCapabilities];
-[AUAudioUnitV2Bridge deliverV2Parameters:];
-[AUAudioUnitV2Bridge init2];
-[AUAudioUnitV2Bridge inputBusses];
-[AUAudioUnitV2Bridge internalDeallocateRenderResources];
-[AUAudioUnitV2Bridge internalRenderBlock];
-[AUAudioUnitV2Bridge invalidateAudioUnit];
-[AUAudioUnitV2Bridge osWorkgroup];
-[AUAudioUnitV2Bridge outputBusses];
-[AUAudioUnitV2Bridge parameterTree];
-[AUAudioUnitV2Bridge providesUserInterface];
-[AUAudioUnitV2Bridge setFullState:];
-[AUAudioUnitV2Bridge setFullStateForDocument:];
-[AUAudioUnitV2Bridge setMIDIOutputEventBlock:];
-[AUAudioUnitV2Bridge setMIDIOutputEventListBlock:];
-[AUAudioUnitV2Bridge setMusicalContextBlock:];
-[AUAudioUnitV2Bridge setTransportStateBlock:];
```
