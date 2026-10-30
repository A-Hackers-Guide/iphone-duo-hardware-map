# `SBDodgingTesterView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBDodgingItemDelegate`, `UITableViewDelegate`, `UITableViewDataSource`
- 17 instance variables, 21 properties, 48 instance methods, 0 class methods

## Instance variables

```
B _stashed;
@"SBDodgingItem" _item;
@"SBDodgingResolverViewController" _controller;
@"NSString" _name;
@"UIColor" _color;
@"NSMutableSet" _ignoringItems;
Q _corner;
@"UIPanGestureRecognizer" _moveGesture;
@"UIPanGestureRecognizer" _resizeGesture;
@"UILabel" _titleLabel;
@"UILabel" _resolvedValuesLabel;
@"UIView" _resizeView;
@"NSArray" _otherIdentifiers;
@"UITableView" _otherItemsTable;
{CGSize="width"d"height"d} _preferredSize;
{CGPoint="x"d"y"d} _preferredCenter;
{CGPoint="x"d"y"d} _initialMoveCenter;
```

## Properties

```
@property (T@"SBDodgingItem",&,N,V_item) item;
@property (T@"SBDodgingResolverViewController",W,N,V_controller) controller;
@property (T@"NSString",&,N,V_name) name;
@property (T@"UIColor",&,N,V_color) color;
@property (T{CGSize=dd},N,V_preferredSize) preferredSize;
@property (T{CGPoint=dd},N,V_preferredCenter) preferredCenter;
@property (T@"NSMutableSet",&,N,V_ignoringItems) ignoringItems;
@property (TQ,N,V_corner) corner;
@property (TB,N,V_stashed) stashed;
@property (T@"UIPanGestureRecognizer",&,N,V_moveGesture) moveGesture;
@property (T{CGPoint=dd},N,V_initialMoveCenter) initialMoveCenter;
@property (T@"UIPanGestureRecognizer",&,N,V_resizeGesture) resizeGesture;
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"UILabel",&,N,V_resolvedValuesLabel) resolvedValuesLabel;
@property (T@"UIView",&,N,V_resizeView) resizeView;
@property (T@"NSArray",&,N,V_otherIdentifiers) otherIdentifiers;
@property (T@"UITableView",&,N,V_otherItemsTable) otherItemsTable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDodgingTesterView tableView:numberOfRowsInSection:];
-[SBDodgingTesterView numberOfSectionsInTableView:];
-[SBDodgingTesterView tableView:cellForRowAtIndexPath:];
-[SBDodgingTesterView setColor:];
-[SBDodgingTesterView controller];
-[SBDodgingTesterView setTitleLabel:];
-[SBDodgingTesterView titleLabel];
-[SBDodgingTesterView setItem:];
-[SBDodgingTesterView layoutSubviews];
-[SBDodgingTesterView setController:];
-[SBDodgingTesterView item];
-[SBDodgingTesterView color];
-[SBDodgingTesterView tableView:didSelectRowAtIndexPath:];
-[SBDodgingTesterView setPreferredSize:];
-[SBDodgingTesterView setName:];
-[SBDodgingTesterView name];
-[SBDodgingTesterView preferredSize];
-[SBDodgingTesterView corner];
-[SBDodgingTesterView _handleResizeGesture:];
-[SBDodgingTesterView stashed];
-[SBDodgingTesterView setStashed:];
-[SBDodgingTesterView otherItemsTable];
-[SBDodgingTesterView preferredCenter];
-[SBDodgingTesterView setMoveGesture:];
-[SBDodgingTesterView _handleChangeAnchorGesture:];
-[SBDodgingTesterView _handleDeleteGesture:];
-[SBDodgingTesterView _handleMoveGesture:];
-[SBDodgingTesterView _updateResolvedValuesLabel];
-[SBDodgingTesterView dodgingResolver:dodgingItemDidChange:];
-[SBDodgingTesterView dodgingResolver:dodgingItemDidSettle:];
-[SBDodgingTesterView dodgingResolver:preferenceForDodgingItem:];
-[SBDodgingTesterView ignoringItems];
-[SBDodgingTesterView initWithName:color:controller:];
-[SBDodgingTesterView initialMoveCenter];
-[SBDodgingTesterView moveGesture];
-[SBDodgingTesterView otherIdentifiers];
-[SBDodgingTesterView resizeGesture];
-[SBDodgingTesterView resizeView];
-[SBDodgingTesterView resolvedValuesLabel];
-[SBDodgingTesterView setCorner:];
-[SBDodgingTesterView setIgnoringItems:];
-[SBDodgingTesterView setInitialMoveCenter:];
-[SBDodgingTesterView setOtherIdentifiers:];
-[SBDodgingTesterView setOtherItemsTable:];
-[SBDodgingTesterView setPreferredCenter:];
-[SBDodgingTesterView setResizeGesture:];
-[SBDodgingTesterView setResizeView:];
-[SBDodgingTesterView setResolvedValuesLabel:];
```
