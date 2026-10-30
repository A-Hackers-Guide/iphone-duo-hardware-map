# `_UIColorSampler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<EDServiceServer>" _eyeDropperServerProxy;
@"_UIColorSamplerSettings" _settings;
@"NSXPCConnection" _eyeDropperConnection;
@? _eyeDropperSelectionBlock;
B _floatEyedropperOnStart;
```

## Instance methods

```
-[_UIColorSampler init];
-[_UIColorSampler initWithSettings:];
-[_UIColorSampler floatEyedropper];
-[_UIColorSampler _createServerProxyIfNeeded];
-[_UIColorSampler dismissEyedropper];
-[_UIColorSampler eyedropperDidSelectColor:];
-[_UIColorSampler floatEyedropperOnStart];
-[_UIColorSampler invokeEyedropper];
-[_UIColorSampler setFloatEyedropperOnStart:];
-[_UIColorSampler showSamplerWithSelectionHandler:];
```
