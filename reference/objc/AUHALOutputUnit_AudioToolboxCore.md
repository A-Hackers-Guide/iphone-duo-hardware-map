# `AUHALOutputUnit`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnitV2Bridge`
- 7 instance variables, 2 properties, 22 instance methods, 0 class methods

## Instance variables

```
@? _outputProvider;
@? _inputHandler;
B _inputWasEnabled;
B _outputWasEnabled;
B _inputBusEnabled;
{RenderObserverList="mObservers"{TThreadSafeList<RenderObserver>="mActiveList"{NodeStack="mHead"^{Node}}"mPendingList"{NodeStack="mHead"^{Node}}"mFreeList"{NodeStack="mHead"^{Node}}}"mTouched"B} _renderObserverList;
B _renderNotifyInstalled;
```

## Properties

```
@property (TB,N,GisInputEnabled) inputEnabled;
@property (TB,N,GisOutputEnabled) outputEnabled;
```

## Instance methods

```
-[AUHALOutputUnit isRunning];
-[AUHALOutputUnit setOutputProvider:];
-[AUHALOutputUnit canPerformInput];
-[AUHALOutputUnit stopHardware];
-[AUHALOutputUnit initAUHALOutputUnit];
-[AUHALOutputUnit initWithComponentDescription:options:error:];
-[AUHALOutputUnit dealloc];
-[AUHALOutputUnit setOutputEnabled:];
-[AUHALOutputUnit setInputEnabled:];
-[AUHALOutputUnit tokenByAddingRenderObserver:];
-[AUHALOutputUnit addRenderObserver:userData:];
-[AUHALOutputUnit outputProvider];
-[AUHALOutputUnit _inputHandler];
-[AUHALOutputUnit isInputEnabled];
-[AUHALOutputUnit startHardwareAndReturnError:];
-[AUHALOutputUnit canPerformOutput];
-[AUHALOutputUnit removeRenderObserver:userData:];
-[AUHALOutputUnit initWithAudioUnit:description:];
-[AUHALOutputUnit setInputHandler:];
-[AUHALOutputUnit enableBus:scope:enable:];
-[AUHALOutputUnit isOutputEnabled];
-[AUHALOutputUnit removeRenderObserver:];
```
