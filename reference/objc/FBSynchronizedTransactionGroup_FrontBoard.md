# `FBSynchronizedTransactionGroup`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBTransaction`
- Protocols: `FBSynchronizedTransaction`, `FBSynchronizedTransactionDelegate`
- 7 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _commitAllowed;
B _readyForCommit;
B _didCommit;
@"NSMutableSet" _synchronizedTransactions;
@"NSMutableSet" _synchronizedTransactionsAwaitingCommitReadiness;
@"NSMutableSet" _synchronizedTransactionsReadyToCommit;
@"<FBSynchronizedTransactionGroupDelegate>" _synchronizationDelegate;
```

## Properties

```
@property (T@"<FBSynchronizedTransactionDelegate>",W,N,V_synchronizationDelegate) synchronizationDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSynchronizedTransactionGroup _childTransactionDidComplete:];
-[FBSynchronizedTransactionGroup isReadyForSynchronizedCommit];
-[FBSynchronizedTransactionGroup performSynchronizedCommit];
-[FBSynchronizedTransactionGroup _canBeInterrupted];
-[FBSynchronizedTransactionGroup _checkPreconditionsAndCommitIfReady];
-[FBSynchronizedTransactionGroup _didComplete];
-[FBSynchronizedTransactionGroup setSynchronizationDelegate:];
-[FBSynchronizedTransactionGroup _performSynchronizedCommit:];
-[FBSynchronizedTransactionGroup synchronizedTransaction:willCommitSynchronizedTransactions:];
-[FBSynchronizedTransactionGroup synchronizedTransaction:didCommitSynchronizedTransactions:];
-[FBSynchronizedTransactionGroup synchronizationDelegate];
-[FBSynchronizedTransactionGroup init];
-[FBSynchronizedTransactionGroup synchronizedTransactions];
-[FBSynchronizedTransactionGroup _shouldFailForChildTransaction:];
-[FBSynchronizedTransactionGroup _performSynchronizedCommitIfReady];
-[FBSynchronizedTransactionGroup synchronizedTransactionReadyToCommit:];
-[FBSynchronizedTransactionGroup addSynchronizedTransaction:];
```
