# `UIActionSheet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPopoverControllerDelegate`
- 15 instance variables, 13 properties, 49 instance methods, 0 class methods

## Instance variables

```
@"UIAlertController" _alertController;
@"_UIAlertControllerShimPresenter" _presenter;
@"UIActionSheet" _retainedSelf;
@"NSMutableArray" _actions;
q _cancelIndex;
q _firstOtherButtonIndex;
q _destructiveButtonIndex;
q _actionSheetStyle;
B _hasPreparedAlertActions;
B _isPresented;
B _alertControllerShouldDismiss;
B _handlingAlertActionShouldDismiss;
B _dismissingAlertController;
@"<UIActionSheetDelegate>" _delegate;
@ _context;
```

## Properties

```
@property (T@,&,N,V_context) context;
@property (T@"<UIActionSheetDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",C,N) title;
@property (Tq,N) actionSheetStyle;
@property (Tq,R,N) numberOfButtons;
@property (Tq,N) cancelButtonIndex;
@property (Tq,N) destructiveButtonIndex;
@property (Tq,R,N) firstOtherButtonIndex;
@property (TB,R,N,GisVisible) visible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIActionSheet setMessage:];
-[UIActionSheet subtitle];
-[UIActionSheet message];
-[UIActionSheet dealloc];
-[UIActionSheet isVisible];
-[UIActionSheet _didPresent];
-[UIActionSheet setSubtitle:];
-[UIActionSheet setDelegate:];
-[UIActionSheet bodyText];
-[UIActionSheet setContext:];
-[UIActionSheet title];
-[UIActionSheet delegate];
-[UIActionSheet setTitle:];
-[UIActionSheet _alertController];
-[UIActionSheet context];
-[UIActionSheet initWithFrame:];
-[UIActionSheet numberOfButtons];
-[UIActionSheet showFromTabBar:];
-[UIActionSheet setTaglineText:];
-[UIActionSheet showFromBarButtonItem:animated:];
-[UIActionSheet _dismissForTappedIndex:];
-[UIActionSheet _performPresentationDismissalWithClickedButtonIndex:animated:];
-[UIActionSheet _prepareAlertActions];
-[UIActionSheet _prepareToDismissForTappedIndex:];
-[UIActionSheet _preparedAlertActionAtIndex:];
-[UIActionSheet _setAttributedTitleString:];
-[UIActionSheet _setFirstOtherButtonIndex:];
-[UIActionSheet _setIsPresented:];
-[UIActionSheet _showFromRect:inView:direction:animated:];
-[UIActionSheet _titleLabel];
-[UIActionSheet actionSheetStyle];
-[UIActionSheet addButtonWithTitle:];
-[UIActionSheet addButtonWithTitle:label:];
-[UIActionSheet buttonTitleAtIndex:];
-[UIActionSheet cancelButtonIndex];
-[UIActionSheet destructiveButtonIndex];
-[UIActionSheet dismissWithClickedButtonIndex:animated:];
-[UIActionSheet firstOtherButtonIndex];
-[UIActionSheet initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:];
-[UIActionSheet initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:];
-[UIActionSheet popoverControllerDidDismissPopover:];
-[UIActionSheet presentFromRect:inView:direction:allowInteractionWithViews:backgroundStyle:animated:];
-[UIActionSheet setActionSheetStyle:];
-[UIActionSheet setBodyText:];
-[UIActionSheet setCancelButtonIndex:];
-[UIActionSheet setDestructiveButtonIndex:];
-[UIActionSheet showFromRect:inView:animated:];
-[UIActionSheet showFromToolbar:];
-[UIActionSheet showInView:];
```
