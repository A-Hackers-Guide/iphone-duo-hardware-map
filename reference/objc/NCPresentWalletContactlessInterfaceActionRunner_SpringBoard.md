# `NCPresentWalletContactlessInterfaceActionRunner`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NCNotificationActionRunner`
- 3 instance variables, 7 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _shouldForwardAction;
@"NSString" _passUniqueID;
@"SBSCardItem" _cardItem;
```

## Properties

```
@property (T@"NSString",R,&,N,V_passUniqueID) passUniqueID;
@property (T@"SBSCardItem",R,&,N,V_cardItem) cardItem;
@property (TB,N,V_shouldForwardAction) shouldForwardAction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NCPresentWalletContactlessInterfaceActionRunner passUniqueID];
-[NCPresentWalletContactlessInterfaceActionRunner cardItem];
-[NCPresentWalletContactlessInterfaceActionRunner executeAction:fromOrigin:endpoint:withParameters:completion:];
-[NCPresentWalletContactlessInterfaceActionRunner setShouldForwardAction:];
-[NCPresentWalletContactlessInterfaceActionRunner shouldForwardAction];
-[NCPresentWalletContactlessInterfaceActionRunner initWithPassUniqueID:cardItem:];
```
