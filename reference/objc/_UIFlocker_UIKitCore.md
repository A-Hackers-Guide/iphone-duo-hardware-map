# `_UIFlocker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _isFlocked;
Q _itemCount;
Q _badgeValue;
Q _settings;
@"UITargetedPreview" _primaryPlatterPreview;
@"NSArray" _secondaryPlatterViews;
@? _unflockPreviewProvider;
@"<_UIGroupCompletionProviding>" _groupCompletion;
@"UIView" _containerView;
@"_UIDragBadge" _badge;
@"NSMutableArray" _ghostPortals;
```

## Properties

```
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"_UIDragBadge",&,N,V_badge) badge;
@property (T@"NSMutableArray",&,N,V_ghostPortals) ghostPortals;
@property (TB,N,V_isFlocked) isFlocked;
@property (TQ,N,V_itemCount) itemCount;
@property (TQ,N,V_badgeValue) badgeValue;
@property (TQ,N,V_settings) settings;
@property (T@"UITargetedPreview",&,N,V_primaryPlatterPreview) primaryPlatterPreview;
@property (T@"NSArray",&,N,V_secondaryPlatterViews) secondaryPlatterViews;
@property (T@?,C,N,V_unflockPreviewProvider) unflockPreviewProvider;
@property (T@"<_UIGroupCompletionProviding>",&,N,V_groupCompletion) groupCompletion;
```

## Instance methods

```
-[_UIFlocker badgeValue];
-[_UIFlocker itemCount];
-[_UIFlocker setBadgeValue:];
-[_UIFlocker setContainerView:];
-[_UIFlocker badge];
-[_UIFlocker setSettings:];
-[_UIFlocker setBadge:];
-[_UIFlocker settings];
-[_UIFlocker groupCompletion];
-[_UIFlocker setItemCount:];
-[_UIFlocker hitTest:withEvent:];
-[_UIFlocker containerView];
-[_UIFlocker initWithContainerView:];
-[_UIFlocker install];
-[_UIFlocker unflock];
-[_UIFlocker _badgeCenter];
-[_UIFlocker _installGhostPortalForPreview:];
-[_UIFlocker _primaryPlatterView];
-[_UIFlocker badgeLocationInView:];
-[_UIFlocker flock];
-[_UIFlocker ghostPortals];
-[_UIFlocker isFlocked];
-[_UIFlocker primaryPlatterPreview];
-[_UIFlocker secondaryPlatterViews];
-[_UIFlocker setGhostPortals:];
-[_UIFlocker setGroupCompletion:];
-[_UIFlocker setIsFlocked:];
-[_UIFlocker setPrimaryPlatterPreview:];
-[_UIFlocker setSecondaryPlatterViews:];
-[_UIFlocker setUnflockPreviewProvider:];
-[_UIFlocker unflockPreviewProvider];
-[_UIFlocker unflockToDrag:animated:];
-[_UIFlocker updateFlockLocation];
```
