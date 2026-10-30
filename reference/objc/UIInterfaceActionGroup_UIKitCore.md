# `UIInterfaceActionGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInterfaceActionDisplayPropertyObserver`, `NSCopying`
- 8 instance variables, 12 properties, 27 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _actions;
@"UIInterfaceAction" _preferredAction;
@"NSPointerArray" _weakDisplayPropertyObservers;
@"NSString" _title;
@"NSArray" _actionsBySection;
@"UIInterfaceActionVisualStyle" _visualStyle;
{CGSize="width"d"height"d} _leadingImageLayoutSize;
{CGSize="width"d"height"d} _trailingImageLayoutSize;
```

## Properties

```
@property (T@"NSPointerArray",R,N,V_weakDisplayPropertyObservers) weakDisplayPropertyObservers;
@property (T@"NSString",R,N,V_title) title;
@property (T@"NSArray",R,N,V_actionsBySection) actionsBySection;
@property (T{CGSize=dd},R,N,V_leadingImageLayoutSize) leadingImageLayoutSize;
@property (T{CGSize=dd},R,N,V_trailingImageLayoutSize) trailingImageLayoutSize;
@property (T@"UIInterfaceActionVisualStyle",&,N,G_visualStyle,S_setVisualStyle:,V_visualStyle) visualStyle;
@property (T@"NSArray",R,N,V_actions) actions;
@property (T@"UIInterfaceAction",&,N,V_preferredAction) preferredAction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIInterfaceActionGroup actionGroupWithActions:];
+[UIInterfaceActionGroup actionGroupWithActionsBySection:];
+[UIInterfaceActionGroup changedProperties:containsAny:];
```

## Instance methods

```
-[UIInterfaceActionGroup setLeadingImageLayoutSize:];
-[UIInterfaceActionGroup _reloadImageLayoutSizesUsingExistingActionImages];
-[UIInterfaceActionGroup _notifyObserversVisualStyleDidChange];
-[UIInterfaceActionGroup _performWithActionObservingDisabled:];
-[UIInterfaceActionGroup setPreferredAction:];
-[UIInterfaceActionGroup initWithTitle:actionsBySection:];
-[UIInterfaceActionGroup _addActionGroupDisplayPropertyObserver:];
-[UIInterfaceActionGroup actions];
-[UIInterfaceActionGroup _visualStyle];
-[UIInterfaceActionGroup setTrailingImageLayoutSize:];
-[UIInterfaceActionGroup _deepCopyOfActionsBySection];
-[UIInterfaceActionGroup _updateActionImageLayoutSizes];
-[UIInterfaceActionGroup title];
-[UIInterfaceActionGroup _setVisualStyle:];
-[UIInterfaceActionGroup _notifyObserversDidChangeActionProperty:];
-[UIInterfaceActionGroup description];
-[UIInterfaceActionGroup trailingImageLayoutSize];
-[UIInterfaceActionGroup interfaceAction:reloadDisplayedContentVisualStyle:];
-[UIInterfaceActionGroup actionsBySection];
-[UIInterfaceActionGroup copyWithZone:];
-[UIInterfaceActionGroup preferredAction];
-[UIInterfaceActionGroup interfaceAction:reloadDisplayedContentActionProperties:];
-[UIInterfaceActionGroup _beginObservingActions];
-[UIInterfaceActionGroup _removeActionGroupDisplayPropertyObserver:];
-[UIInterfaceActionGroup weakDisplayPropertyObservers];
-[UIInterfaceActionGroup _endObservingActions];
-[UIInterfaceActionGroup leadingImageLayoutSize];
```
