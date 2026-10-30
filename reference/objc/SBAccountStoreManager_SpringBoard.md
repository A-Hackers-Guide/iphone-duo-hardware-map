# `SBAccountStoreManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"ACAccountStore" _accountStore;
@"ACAccount" _primaryAppleAccount;
```

## Properties

```
@property (T@"ACAccount",&,N,V_primaryAppleAccount) primaryAppleAccount;
@property (T@"ACAccountStore",R,N,V_accountStore) accountStore;
```

## Instance methods

```
-[SBAccountStoreManager accountStore];
-[SBAccountStoreManager init];
-[SBAccountStoreManager _accountStoreDidChange:];
-[SBAccountStoreManager setPrimaryAppleAccount:];
-[SBAccountStoreManager primaryAppleAccount];
-[SBAccountStoreManager _queue_updatePrimaryAppleAccount];
-[SBAccountStoreManager _updatePrimaryAppleAccount];
```
