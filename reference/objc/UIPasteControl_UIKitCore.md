# `UIPasteControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `_UISecureControl`
- 5 instance variables, 2 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"_UISecureController" _secureController;
B _pasteboardObserved;
B _internallyEnabled;
@"UIPasteControlConfiguration" _configuration;
@"<UIPasteConfigurationSupporting>" _target;
```

## Properties

```
@property (T@"UIPasteControlConfiguration",R,N,V_configuration) configuration;
@property (T@"<UIPasteConfigurationSupporting>",W,N,V_target) target;
```

## Instance methods

```
-[UIPasteControl intrinsicContentSize];
-[UIPasteControl endTrackingWithTouch:withEvent:];
-[UIPasteControl layoutSubviews];
-[UIPasteControl initWithConfiguration:];
-[UIPasteControl _encodableSubviews];
-[UIPasteControl sizeThatFits:];
-[UIPasteControl setHighlighted:];
-[UIPasteControl configuration];
-[UIPasteControl setEnabled:];
-[UIPasteControl setTarget:];
-[UIPasteControl encodeWithCoder:];
-[UIPasteControl initWithCoder:];
-[UIPasteControl target];
-[UIPasteControl initWithFrame:];
-[UIPasteControl _updateEnabledWithNotification:];
-[UIPasteControl synchronousSecureControlService];
-[UIPasteControl _secureName];
-[UIPasteControl isInternallyEnabled];
-[UIPasteControl shouldTrack];
```
