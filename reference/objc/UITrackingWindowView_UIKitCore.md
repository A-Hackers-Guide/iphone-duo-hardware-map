# `UITrackingWindowView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITrackingElementHostView`
- Protocols: `_UIViewHost`
- 4 instance variables, 6 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"UIKBRenderConfig" _renderConfig;
@"NSMutableDictionary" _hostedViews;
B _disableGeometryObserverNotifications;
{CGPoint="x"d"y"d} _offsetOrigin;
```

## Properties

```
@property (T{CGPoint=dd},N,V_offsetOrigin) offsetOrigin;
@property (T@"UIScreen",R) hostingScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITrackingWindowView _shouldHitTestInputViewFirst];
+[UITrackingWindowView _notifyOnExplicitLayout];
```

## Instance methods

```
-[UITrackingWindowView didAddSubview:];
-[UITrackingWindowView _inheritedRenderConfig];
-[UITrackingWindowView _setAccessoryViewFrame:];
-[UITrackingWindowView hasHostedViews];
-[UITrackingWindowView addSubview:];
-[UITrackingWindowView _setRenderConfig:];
-[UITrackingWindowView dealloc];
-[UITrackingWindowView setCenter:];
-[UITrackingWindowView setOffsetOrigin:];
-[UITrackingWindowView _accessoryViewFrame];
-[UITrackingWindowView offsetOrigin];
-[UITrackingWindowView hostingScreen];
-[UITrackingWindowView _inputWindowController];
-[UITrackingWindowView setFrame:];
-[UITrackingWindowView _didRemoveSubview:];
-[UITrackingWindowView performWithoutGeometryObserverNotifications:];
-[UITrackingWindowView addHostedView:withViewRemovalHandler:];
-[UITrackingWindowView initWithFrame:];
-[UITrackingWindowView _disableGeometryObserverNotification];
```
