# `UICellAccessoryManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 17 properties, 40 instance methods, 0 class methods

## Instance variables

```
{CGSize="width"d"height"d} _enforcedContainerSize;
B _needsLayout;
@? _standardLayoutWidthProvider;
@? _disclosureLayoutWidthProvider;
@"<UICellAccessoryLayout>" _leadingLayout;
@"<UICellAccessoryLayout>" _trailingLayout;
@"NSDictionary" _configurations;
@"NSString" _currentConfigurationIdentifier;
@"UIView" _containerView;
@"UICellAccessoryConfiguration" _previousConfiguration;
@"NSMutableDictionary" _accessoryViews;
q _animatedLayoutUpdatesCount;
{CGSize="width"d"height"d} _previousContainerSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _safeAreaInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInset;
```

## Properties

```
@property (T@"UIView",W,N,V_containerView) containerView;
@property (TB,N,V_needsLayout) needsLayout;
@property (T{CGSize=dd},N,V_previousContainerSize) previousContainerSize;
@property (T@"UICellAccessoryConfiguration",&,N,V_previousConfiguration) previousConfiguration;
@property (T@"NSMutableDictionary",&,N,V_accessoryViews) accessoryViews;
@property (Tq,N,V_animatedLayoutUpdatesCount) animatedLayoutUpdatesCount;
@property (T{UIEdgeInsets=dddd},N,V_safeAreaInsets) safeAreaInsets;
@property (T@?,C,N,V_standardLayoutWidthProvider) standardLayoutWidthProvider;
@property (T@?,C,N,V_disclosureLayoutWidthProvider) disclosureLayoutWidthProvider;
@property (T@"<UICellAccessoryLayout>",&,N,V_leadingLayout) leadingLayout;
@property (T@"<UICellAccessoryLayout>",&,N,V_trailingLayout) trailingLayout;
@property (T@"NSDictionary",&,N,V_configurations) configurations;
@property (T@"NSString",C,N,V_currentConfigurationIdentifier) currentConfigurationIdentifier;
@property (T@"UICellAccessoryConfiguration",R,N) currentConfiguration;
@property (T{CGSize=dd},R,N) containerSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentFrame;
@property (T{UIEdgeInsets=dddd},R,N,V_contentInset) contentInset;
```

## Instance methods

```
-[UICellAccessoryManager setNeedsLayout];
-[UICellAccessoryManager containerSize];
-[UICellAccessoryManager setContainerView:];
-[UICellAccessoryManager setSafeAreaInsets:];
-[UICellAccessoryManager setAnimatedLayoutUpdatesCount:];
-[UICellAccessoryManager safeAreaInsets];
-[UICellAccessoryManager layoutIfNeeded];
-[UICellAccessoryManager leadingLayout];
-[UICellAccessoryManager setLeadingLayout:];
-[UICellAccessoryManager contentFrame];
-[UICellAccessoryManager currentConfiguration];
-[UICellAccessoryManager updateContainerView:];
-[UICellAccessoryManager setDisclosureLayoutWidthProvider:];
-[UICellAccessoryManager configurations];
-[UICellAccessoryManager _updateAccessories:previousAccessories:withLayout:edge:];
-[UICellAccessoryManager setTrailingLayout:];
-[UICellAccessoryManager setPreviousConfiguration:];
-[UICellAccessoryManager setCurrentConfigurationIdentifier:];
-[UICellAccessoryManager performWithEnforcedContainerSize:block:];
-[UICellAccessoryManager currentConfigurationIdentifier];
-[UICellAccessoryManager trailingLayout];
-[UICellAccessoryManager setAccessoryViews:];
-[UICellAccessoryManager containerView];
-[UICellAccessoryManager animatedLayoutUpdatesCount];
-[UICellAccessoryManager previousContainerSize];
-[UICellAccessoryManager setPreviousContainerSize:];
-[UICellAccessoryManager accessoryViews];
-[UICellAccessoryManager initWithContainerView:];
-[UICellAccessoryManager _configurationWithIdentifier:];
-[UICellAccessoryManager _updateFromPreviousConfiguration:];
-[UICellAccessoryManager setStandardLayoutWidthProvider:];
-[UICellAccessoryManager description];
-[UICellAccessoryManager setNeedsLayout:];
-[UICellAccessoryManager containerBounds];
-[UICellAccessoryManager disclosureLayoutWidthProvider];
-[UICellAccessoryManager previousConfiguration];
-[UICellAccessoryManager standardLayoutWidthProvider];
-[UICellAccessoryManager needsLayout];
-[UICellAccessoryManager contentInset];
-[UICellAccessoryManager setConfigurations:];
```
