# `_UIEditMenuOverlayUIClientPresentation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIEditMenuPresentation`
- Protocols: `_UIOverlayServiceDelegate`, `_UIOMenuPresentationClient`
- 3 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"_UIOEditMenuPresentationConfiguration" _presentationConfiguration;
@"_UIOverlayService" _overlayService;
@"_UIHostedMenuManager" _menuManager;
```

## Properties

```
@property (T@"_UIOverlayService",R,N,V_overlayService) overlayService;
@property (T@"_UIHostedMenuManager",R,N,V_menuManager) menuManager;
@property (T@"_UIOEditMenuPresentationConfiguration",R,N,V_presentationConfiguration) presentationConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIEditMenuOverlayUIClientPresentation didTransitionFrom:to:];
-[_UIEditMenuOverlayUIClientPresentation displayedMenu];
-[_UIEditMenuOverlayUIClientPresentation presentationConfiguration];
-[_UIEditMenuOverlayUIClientPresentation _configureOverlayServiceIfNeeded];
-[_UIEditMenuOverlayUIClientPresentation displayMenu:configuration:];
-[_UIEditMenuOverlayUIClientPresentation handleLifecycleEvent:];
-[_UIEditMenuOverlayUIClientPresentation hideMenuWithReason:];
-[_UIEditMenuOverlayUIClientPresentation initWithDelegate:sourceView:];
-[_UIEditMenuOverlayUIClientPresentation menuManager];
-[_UIEditMenuOverlayUIClientPresentation overlayService];
-[_UIEditMenuOverlayUIClientPresentation overlayServiceDidInvalidate:];
-[_UIEditMenuOverlayUIClientPresentation performMenuLeafAction:completionHandler:];
-[_UIEditMenuOverlayUIClientPresentation preparedMenuWithIdentifier:completionHandler:];
-[_UIEditMenuOverlayUIClientPresentation replaceVisibleMenuWithMenu:reason:];
-[_UIEditMenuOverlayUIClientPresentation setDisplayedMenu:];
-[_UIEditMenuOverlayUIClientPresentation sourceViewDidUpdateFromTraitCollection:];
```
