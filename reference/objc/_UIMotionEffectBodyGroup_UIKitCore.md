# `_UIMotionEffectBodyGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMotionEffectEventConsumer`
- 14 instance variables, 17 properties, 30 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pendingEventLock;
B _hasReceivedAtLeastOneEvent;
@"_UIMotionEffectBody" _body;
@"CMMotionManager" _motionManager;
@"_UIMotionEffectEventProvider" _eventProvider;
@"NSString" _bodyKey;
@"_UIMotionEffectEvent" _pendingEvent;
@"_UIMotionEffectEvent" _lastProcessedEvent;
@"_UIMotionEffectEvent" _lastEvent;
@"_UILazyMapTable" _analyzerSettingsToAnalyzers;
@"NSMapTable" _analyzersToEffects;
@"NSHashTable" _views;
@"_UIMotionEffectEngine" _engine;
@"_UIMotionEffectScreenState" _screenState;
```

## Properties

```
@property (T@"NSString",C,N,V_bodyKey) bodyKey;
@property (T@"CMMotionManager",&,N,V_motionManager) motionManager;
@property (T@"_UIMotionEffectBody",&,N,V_body) body;
@property (T@"_UIMotionEffectEventProvider",&,N,V_eventProvider) eventProvider;
@property (T@"_UIMotionEffectEvent",&,N,V_pendingEvent) pendingEvent;
@property (T@"_UIMotionEffectEvent",&,N,V_lastProcessedEvent) lastProcessedEvent;
@property (T@"_UIMotionEffectEvent",&,N,V_lastEvent) lastEvent;
@property (TB,N,V_hasReceivedAtLeastOneEvent) hasReceivedAtLeastOneEvent;
@property (T@"_UILazyMapTable",&,N,V_analyzerSettingsToAnalyzers) analyzerSettingsToAnalyzers;
@property (T@"NSMapTable",&,N,V_analyzersToEffects) analyzersToEffects;
@property (T@"NSHashTable",&,N,V_views) views;
@property (T@"_UIMotionEffectEngine",W,N,V_engine) engine;
@property (T@"_UIMotionEffectScreenState",W,N,V_screenState) screenState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIMotionEffectBodyGroup _newConfiguredMotionManager];
```

## Instance methods

```
-[_UIMotionEffectBodyGroup views];
-[_UIMotionEffectBodyGroup setEngine:];
-[_UIMotionEffectBodyGroup engine];
-[_UIMotionEffectBodyGroup body];
-[_UIMotionEffectBodyGroup setBody:];
-[_UIMotionEffectBodyGroup init];
-[_UIMotionEffectBodyGroup lastProcessedEvent];
-[_UIMotionEffectBodyGroup screenState];
-[_UIMotionEffectBodyGroup setViews:];
-[_UIMotionEffectBodyGroup setLastEvent:];
-[_UIMotionEffectBodyGroup lastEvent];
-[_UIMotionEffectBodyGroup setLastProcessedEvent:];
-[_UIMotionEffectBodyGroup updateWithEvent:];
-[_UIMotionEffectBodyGroup updateEventProviderStatus:];
-[_UIMotionEffectBodyGroup bodyKey];
-[_UIMotionEffectBodyGroup setAnalyzerSettingsToAnalyzers:];
-[_UIMotionEffectBodyGroup setScreenState:];
-[_UIMotionEffectBodyGroup analyzerSettingsToAnalyzers];
-[_UIMotionEffectBodyGroup analyzersToEffects];
-[_UIMotionEffectBodyGroup eventProvider];
-[_UIMotionEffectBodyGroup hasReceivedAtLeastOneEvent];
-[_UIMotionEffectBodyGroup motionManager];
-[_UIMotionEffectBodyGroup pendingEvent];
-[_UIMotionEffectBodyGroup setAnalyzersToEffects:];
-[_UIMotionEffectBodyGroup setBodyKey:];
-[_UIMotionEffectBodyGroup setEventProvider:];
-[_UIMotionEffectBodyGroup setHasReceivedAtLeastOneEvent:];
-[_UIMotionEffectBodyGroup setMotionManager:];
-[_UIMotionEffectBodyGroup setPendingEvent:];
-[_UIMotionEffectBodyGroup snapshotPendingEvent];
```
