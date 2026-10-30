# `SBFAlwaysOnLiveRenderingAssertionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightStateObserving`, `BLSAssertionObserving`
- 5 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"BLSAssertion" _liveRenderingAssertion;
@"SBFAlwaysOnLiveRenderingAssertionWeakCollection" _liveRenderingAssertionProxies;
@"<SBFAlwaysOnLiveRenderingBLSAssertionProvider>" _assertionProvider;
@"<SBFAlwaysOnLiveRenderingBLSAttributesProvider>" _attributesProvider;
@"<BLSBacklightStateObservable>" _backlight;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFAlwaysOnLiveRenderingAssertionManager debugDescription];
-[SBFAlwaysOnLiveRenderingAssertionManager acquireLiveRenderingAssertionWithReason:];
-[SBFAlwaysOnLiveRenderingAssertionManager assertion:didCancelWithError:];
-[SBFAlwaysOnLiveRenderingAssertionManager _nextLiveRenderingAssertionProxyIfAny];
-[SBFAlwaysOnLiveRenderingAssertionManager initWithBacklight:assertionProvider:attributesProvider:];
-[SBFAlwaysOnLiveRenderingAssertionManager dealloc];
-[SBFAlwaysOnLiveRenderingAssertionManager backlight:didCompleteUpdateToState:forEvent:];
-[SBFAlwaysOnLiveRenderingAssertionManager assertion:didFailToAcquireWithError:];
-[SBFAlwaysOnLiveRenderingAssertionManager invalidate];
-[SBFAlwaysOnLiveRenderingAssertionManager _releaseLiveRenderingAssertionWithReason:];
-[SBFAlwaysOnLiveRenderingAssertionManager _acquireLiveRenderingAssertionProxy:];
-[SBFAlwaysOnLiveRenderingAssertionManager description];
-[SBFAlwaysOnLiveRenderingAssertionManager backlight:didChangeAlwaysOnEnabled:];
-[SBFAlwaysOnLiveRenderingAssertionManager _acquireLiveRenderingAssertionIfNeededForProxy:backlight:];
-[SBFAlwaysOnLiveRenderingAssertionManager _invalidateWithReason:];
-[SBFAlwaysOnLiveRenderingAssertionManager _releaseLiveRenderingAssertionProxy:];
-[SBFAlwaysOnLiveRenderingAssertionManager backlight];
```
