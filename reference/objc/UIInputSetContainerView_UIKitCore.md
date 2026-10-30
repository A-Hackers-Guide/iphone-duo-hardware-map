# `UIInputSetContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputSetHostView`
- Protocols: `_UIViewHost`
- 5 instance variables, 6 properties, 20 instance methods, 2 class methods

## Instance variables

```
@"UIKBRenderConfig" _renderConfig;
@"NSMutableDictionary" _hostedViews;
B _disableGeometryObserverNotifications;
@"UIInputActiveSetContainerView" _containerForKeyplaneViews;
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
+[UIInputSetContainerView _shouldHitTestInputViewFirst];
+[UIInputSetContainerView _notifyOnExplicitLayout];
```

## Instance methods

```
-[UIInputSetContainerView didAddSubview:];
-[UIInputSetContainerView _inheritedRenderConfig];
-[UIInputSetContainerView _setAccessoryViewFrame:];
-[UIInputSetContainerView hasHostedViews];
-[UIInputSetContainerView addSubview:];
-[UIInputSetContainerView _setRenderConfig:];
-[UIInputSetContainerView dealloc];
-[UIInputSetContainerView setCenter:];
-[UIInputSetContainerView setOffsetOrigin:];
-[UIInputSetContainerView _accessoryViewFrame];
-[UIInputSetContainerView offsetOrigin];
-[UIInputSetContainerView hostingScreen];
-[UIInputSetContainerView _inputWindowController];
-[UIInputSetContainerView setFrame:];
-[UIInputSetContainerView _didRemoveSubview:];
-[UIInputSetContainerView performWithoutGeometryObserverNotifications:];
-[UIInputSetContainerView addHostedView:withViewRemovalHandler:];
-[UIInputSetContainerView initWithFrame:];
-[UIInputSetContainerView _disableGeometryObserverNotification];
-[UIInputSetContainerView _containerForKeyplaneViews];
```
