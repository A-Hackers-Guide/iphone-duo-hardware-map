# `UICoreKeyboardTracking`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUIKeyboardTracker`
- 7 instance variables, 11 properties, 25 instance methods, 3 class methods

## Instance variables

```
B _trackingHasFloatingAssistantView;
B _trackingIsDocked;
B _trackingIsSplit;
@"UIWindow" _window;
@"NSMutableArray" _elements;
{CGSize="width"d"height"d} _trackingSize;
{UIOffset="horizontal"d"vertical"d} _trackingOffset;
```

## Properties

```
@property (T@"UIWindow",R,W,N,V_window) window;
@property (T@"NSMutableArray",&,N,V_elements) elements;
@property (T{CGSize=dd},N,V_trackingSize) trackingSize;
@property (T{UIOffset=dd},N,V_trackingOffset) trackingOffset;
@property (TB,N,V_trackingHasFloatingAssistantView) trackingHasFloatingAssistantView;
@property (TB,N,V_trackingIsDocked) trackingIsDocked;
@property (TB,N,V_trackingIsSplit) trackingIsSplit;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UICoreKeyboardTracking removeTrackingElement:window:keyboardDelegate:];
+[UICoreKeyboardTracking windowMap];
+[UICoreKeyboardTracking addTrackingElement:window:keyboardDelegate:];
```

## Instance methods

```
-[UICoreKeyboardTracking setElements:];
-[UICoreKeyboardTracking sceneForTracker];
-[UICoreKeyboardTracking trackingOffset];
-[UICoreKeyboardTracking elements];
-[UICoreKeyboardTracking setTrackingIsDocked:];
-[UICoreKeyboardTracking initWithWindow:];
-[UICoreKeyboardTracking trackingHasFloatingAssistantView];
-[UICoreKeyboardTracking window];
-[UICoreKeyboardTracking trackingOffsetWillChange:inWindow:animationInfo:];
-[UICoreKeyboardTracking _shouldApplyTrackingOffset];
-[UICoreKeyboardTracking trackingIsSplit];
-[UICoreKeyboardTracking trackingIsDocked];
-[UICoreKeyboardTracking setTrackingHasFloatingAssistantView:];
-[UICoreKeyboardTracking trackingOffsetDidChange:inWindow:animationInfo:];
-[UICoreKeyboardTracking keyboardWillChangeToState:trackingFrame:animationInfo:];
-[UICoreKeyboardTracking _resolvedTrackingSize];
-[UICoreKeyboardTracking trackingSizeWillChange:inWindow:animationInfo:];
-[UICoreKeyboardTracking _dispatchPrepareInWindow:];
-[UICoreKeyboardTracking trackingSize];
-[UICoreKeyboardTracking cleanupElements];
-[UICoreKeyboardTracking setTrackingOffset:];
-[UICoreKeyboardTracking trackingSizeDidChange:inWindow:animationInfo:];
-[UICoreKeyboardTracking setTrackingIsSplit:];
-[UICoreKeyboardTracking setTrackingSize:];
-[UICoreKeyboardTracking keyboardDidChangeToState:trackingFrame:];
```
