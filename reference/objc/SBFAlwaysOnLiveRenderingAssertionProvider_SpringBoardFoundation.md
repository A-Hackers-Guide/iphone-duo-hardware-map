# `SBFAlwaysOnLiveRenderingAssertionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"SBFAlwaysOnLiveRenderingAssertionWeakCollection" _assertions;
@"<BLSBacklightStateObservable>" _backlight;
@"<SBFAlwaysOnLiveRenderingBLSAssertionProvider>" _assertionProvider;
```

## Properties

```
@property (T@"<BLSBacklightStateObservable>",&,N,V_backlight) backlight;
@property (T@"<SBFAlwaysOnLiveRenderingBLSAssertionProvider>",&,N,V_assertionProvider) assertionProvider;
```

## Class methods

```
+[SBFAlwaysOnLiveRenderingAssertionProvider sharedInstance];
```

## Instance methods

```
-[SBFAlwaysOnLiveRenderingAssertionProvider setBacklight:];
-[SBFAlwaysOnLiveRenderingAssertionProvider init];
-[SBFAlwaysOnLiveRenderingAssertionProvider description];
-[SBFAlwaysOnLiveRenderingAssertionProvider backlight];
-[SBFAlwaysOnLiveRenderingAssertionProvider invalidateAllAssertions];
-[SBFAlwaysOnLiveRenderingAssertionProvider _acquireLiveRenderingAssertionForScene:identifier:reason:attributes:];
-[SBFAlwaysOnLiveRenderingAssertionProvider _assertionManagerForScene:];
-[SBFAlwaysOnLiveRenderingAssertionProvider _setAssertionManager:forScene:];
-[SBFAlwaysOnLiveRenderingAssertionProvider acquireLiveRenderingAssertionForFBSScene:reason:];
-[SBFAlwaysOnLiveRenderingAssertionProvider acquireLiveRenderingAssertionForUIScene:reason:];
-[SBFAlwaysOnLiveRenderingAssertionProvider assertionProvider];
-[SBFAlwaysOnLiveRenderingAssertionProvider setAssertionProvider:];
```
