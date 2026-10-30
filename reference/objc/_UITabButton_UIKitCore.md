# `_UITabButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `_UITabBarButton`
- 31 instance variables, 13 properties, 38 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 item;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 configuration;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 appearanceData;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 matchMoveIdentifierForImage;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 matchMoveIdentifierForBadge;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isMinimized;
? tabBar;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 tabBarButtonDelegate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 linkedButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 overrideItemState;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 ignoresSelectedState;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 synchronizeAppearanceAndLayoutChangesToLinkedButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 forwardsMatchMoveIdentifierToLinkedButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 suppressBadge;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 contentOutset;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 imageView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 titleLabel;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 titleWrapper;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 badgeView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 sizeCache;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 unselectedLabelTintColor;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 contentTintColorForState;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 itemContentInsets;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 itemTitleStyle;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 layoutAxis;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 defaultItemDisplayMode;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 overrideItemDisplayMode;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 hasFocusAppearance;
B _showsHighlightedState;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 springLoadedInteraction;
B isSpringLoaded;
```

## Properties

```
@property (T@"UITabBar",N,R,VtabBar) tabBar;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) bounds;
@property (T{CGPoint=dd},N) center;
@property (Td,N) alpha;
@property (T@"UIColor",N,&) unselectedTintColor;
@property (TB,N) selected;
@property (TB,N) highlighted;
@property (TB,N,R) canBecomeFocused;
@property (TB,N) _selected;
@property (TB,N,V_showsHighlightedState) _showsHighlightedState;
@property (TB,N,VisSpringLoaded) springLoaded;
@property (TB,N,R) accessibilityShouldUseSelectedColorWhileFocused;
```

## Instance methods

```
-[_UITabButton _controlEventsForActionTriggered];
-[_UITabButton setSpringLoaded:];
-[_UITabButton isSpringLoaded];
-[_UITabButton _setSelected:];
-[_UITabButton setSelected:];
-[_UITabButton _systemDefaultFocusGroupIdentifier];
-[_UITabButton willMoveToSuperview:];
-[_UITabButton didUpdateFocusInContext:withAnimationCoordinator:];
-[_UITabButton isHighlighted];
-[_UITabButton setCenter:];
-[_UITabButton layoutSubviews];
-[_UITabButton _showSelectedIndicator:changeSelection:];
-[_UITabButton setBounds:];
-[_UITabButton canBecomeFocused];
-[_UITabButton sizeThatFits:];
-[_UITabButton _setBadgeColor:];
-[_UITabButton setAlpha:];
-[_UITabButton tabBar];
-[_UITabButton setHighlighted:];
-[_UITabButton _updateUserInterfaceStyleIfNeeded];
-[_UITabButton center];
-[_UITabButton isSelected];
-[_UITabButton setFrame:];
-[_UITabButton bounds];
-[_UITabButton _showsHighlightedState];
-[_UITabButton _setUnselectedTintColor:];
-[_UITabButton initWithCoder:];
-[_UITabButton alpha];
-[_UITabButton _setShowsHighlightedState:];
-[_UITabButton _setBadgeValue:];
-[_UITabButton _unselectedTintColor];
-[_UITabButton initWithFrame:];
-[_UITabButton _setBadgeTextAttributes:forState:];
-[_UITabButton _invalidateSizeCache];
-[_UITabButton accessibilityShouldUseSelectedColorWhileFocused];
-[_UITabButton frame];
-[_UITabButton _setBadgeOffset:];
-[_UITabButton _isSelected];
```
