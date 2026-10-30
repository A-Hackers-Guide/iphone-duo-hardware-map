# `UIRemoteInputViewHost`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIRemoteInputViewHostWindowDelegate`
- 12 instance variables, 10 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _inputRootViewController;
@"UIInputViewController" _inputViewController;
@"UIView" _inputView;
@"NSLayoutConstraint" _inputViewWidthConstraint;
@"NSLayoutConstraint" _inputViewHeightConstraint;
@"NSLayoutConstraint" _inputViewBottomConstraint;
@"UIViewController" _assistantViewController;
{CGSize="width"d"height"d} _previousInputViewSize;
B _shouldShowDockView;
@"UIWindow" _inputViewWindow;
@"UIWindow" _assistantViewWindow;
@"UIInputViewSet" _inputViewSet;
```

## Properties

```
@property (T@"UIInputViewSet",&,N,V_inputViewSet) inputViewSet;
@property (T@"UIRemoteInputViewInfo",R,N) inputViewInfo;
@property (T@"UIRemoteInputViewInfo",R,N) assistantViewInfo;
@property (TB,N,V_shouldShowDockView) shouldShowDockView;
@property (T@"UIWindow",R,N,V_inputViewWindow) inputViewWindow;
@property (T@"UIWindow",R,N,V_assistantViewWindow) assistantViewWindow;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIRemoteInputViewHost setInputViewSet:];
-[UIRemoteInputViewHost inputViewSet];
-[UIRemoteInputViewHost setShouldShowDockView:];
-[UIRemoteInputViewHost shouldShowDockView];
-[UIRemoteInputViewHost inputViewWindow];
-[UIRemoteInputViewHost assistantViewInfo];
-[UIRemoteInputViewHost assistantViewInsets];
-[UIRemoteInputViewHost assistantViewWindow];
-[UIRemoteInputViewHost inputViewInfo];
-[UIRemoteInputViewHost remoteAssistantItemForResponder:];
-[UIRemoteInputViewHost rtiGroupsForBarButtonItemGroups:];
-[UIRemoteInputViewHost settingsScene];
-[UIRemoteInputViewHost updateAssistantViewIfNecessary];
-[UIRemoteInputViewHost updateCustomInputViewIfNecessary];
-[UIRemoteInputViewHost updateInputViewsIfNecessary];
```
