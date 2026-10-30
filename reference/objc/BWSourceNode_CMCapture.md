# `BWSourceNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 1 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _sourceStartState;
```

## Properties

```
@property (Ti,V_sourceStartState) sourceStartState;
@property (T^{OpaqueCMClock=},R,N) clock;
```

## Class methods

```
+[BWSourceNode initialize];
```

## Instance methods

```
-[BWSourceNode start:];
-[BWSourceNode clock];
-[BWSourceNode makeOutputsLiveWithWillBeStoppedImmediately:];
-[BWSourceNode makeOutputsLiveIfNeeded];
-[BWSourceNode stop:];
-[BWSourceNode nodeType];
-[BWSourceNode setSourceStartState:];
-[BWSourceNode sourceStartState];
-[BWSourceNode transitionStateForMakeOutputsLiveWithWillBeStoppedImmediately:];
-[BWSourceNode transitionToStartedState:];
-[BWSourceNode transitionToStoppedState:];
-[BWSourceNode willStartDeferred];
```
