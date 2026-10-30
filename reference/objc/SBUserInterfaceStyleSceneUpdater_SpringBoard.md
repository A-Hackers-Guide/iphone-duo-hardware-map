# `SBUserInterfaceStyleSceneUpdater`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUserInterfaceStyleObserver`
- 2 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<SBUserInterfaceStyleProvider>" _continuityUserInterfaceStyleProvider;
@"SBDefaultUserInterfaceStyleProvider" _defaultUserInterfaceStyleProvider;
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
-[SBUserInterfaceStyleSceneUpdater dealloc];
-[SBUserInterfaceStyleSceneUpdater initWithContinuityUserInterfaceStyleProvider:];
-[SBUserInterfaceStyleSceneUpdater userInterfaceStyleProvider:didUpdateStyle:preferredAnimationSettings:completion:];
-[SBUserInterfaceStyleSceneUpdater userInterfaceStyleProviderForDisplay:];
```
