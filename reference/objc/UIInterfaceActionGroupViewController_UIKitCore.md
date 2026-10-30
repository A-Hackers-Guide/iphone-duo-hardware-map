# `UIInterfaceActionGroupViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIInterfaceActionHandlerInvocationDelegate`, `UIInterfaceActionGroupDisplaying`, `UISpringLoadedInteractionSupporting`
- 4 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _springLoaded;
@"<UIInterfaceActionVisualStyleProviding>" _visualStyleProvider;
@"UIInterfaceActionGroupView" _actionGroupView;
@"UIInterfaceActionGroup" _actionGroup;
```

## Properties

```
@property (T@"UIInterfaceActionGroup",R,C,N,V_actionGroup) actionGroup;
@property (T@"UIInterfaceActionGroupView",R,C,N,V_actionGroupView) actionGroupView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIInterfaceActionVisualStyle",R,N) visualStyle;
@property (T@"<UIInterfaceActionVisualStyleProviding>",W,N,V_visualStyleProvider) visualStyleProvider;
@property (TB,N,GisSpringLoaded,V_springLoaded) springLoaded;
```

## Instance methods

```
-[UIInterfaceActionGroupViewController setSpringLoaded:];
-[UIInterfaceActionGroupViewController isSpringLoaded];
-[UIInterfaceActionGroupViewController willTransitionToTraitCollection:withTransitionCoordinator:];
-[UIInterfaceActionGroupViewController viewWillDisappear:];
-[UIInterfaceActionGroupViewController visualStyle];
-[UIInterfaceActionGroupViewController viewWillAppear:];
-[UIInterfaceActionGroupViewController defaultVisualStyleForTraitCollection:presentationStyle:];
-[UIInterfaceActionGroupViewController loadView];
-[UIInterfaceActionGroupViewController visualStyleProvider];
-[UIInterfaceActionGroupViewController actionGroupView];
-[UIInterfaceActionGroupViewController setVisualStyleProvider:];
-[UIInterfaceActionGroupViewController actionGroup];
-[UIInterfaceActionGroupViewController initWithActionGroup:];
-[UIInterfaceActionGroupViewController interfaceAction:invokeActionHandler:completion:];
-[UIInterfaceActionGroupViewController reloadVisualStyle];
```
