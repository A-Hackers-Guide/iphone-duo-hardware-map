# `UIKeyboardMotionSupport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIScreenBasedObject`
- 3 instance variables, 7 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"UIScreen" _screen;
@"UIWindowScene" _scene;
@"<UISplitKeyboardSource>" _controller;
```

## Properties

```
@property (T@"<UISplitKeyboardSource>",W,N) masterController;
@property (T@"UIScreen",R) _intendedScreen;
@property (T@"NSDictionary",R) _options;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardMotionSupport supportForScreen:];
+[UIKeyboardMotionSupport supportForUIScene:];
```

## Instance methods

```
-[UIKeyboardMotionSupport _options];
-[UIKeyboardMotionSupport _initWithScreen:options:];
-[UIKeyboardMotionSupport _connectController:];
-[UIKeyboardMotionSupport _matchingOptions:];
-[UIKeyboardMotionSupport _intendedScene];
-[UIKeyboardMotionSupport _disconnectingController:];
-[UIKeyboardMotionSupport _initWithScene:options:];
-[UIKeyboardMotionSupport _updatedController];
-[UIKeyboardMotionSupport _intendedScreen];
-[UIKeyboardMotionSupport generateSplitNotificationForNewPlacement:];
-[UIKeyboardMotionSupport masterController];
-[UIKeyboardMotionSupport setMasterController:];
-[UIKeyboardMotionSupport translateToPlacement:animated:];
-[UIKeyboardMotionSupport translateToPlacement:quietly:animated:];
```
