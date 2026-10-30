# `SBFBackdropLegibilitySettingsProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIBackdropViewObserver`, `SBFLegibilitySettingsProvider`
- 3 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"_UIBackdropView" _backdropView;
@"_UILegibilitySettings" _legibilitySettings;
@"<SBFLegibilitySettingsProviderDelegate>" _delegate;
```

## Properties

```
@property (T@"_UILegibilitySettings",R,N,V_legibilitySettings) legibilitySettings;
@property (T@"<SBFLegibilitySettingsProviderDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFBackdropLegibilitySettingsProvider dealloc];
-[SBFBackdropLegibilitySettingsProvider setDelegate:];
-[SBFBackdropLegibilitySettingsProvider delegate];
-[SBFBackdropLegibilitySettingsProvider legibilitySettings];
-[SBFBackdropLegibilitySettingsProvider backdropViewDidChange:];
-[SBFBackdropLegibilitySettingsProvider initWithBackdropView:];
```
