# `BWDeferredTransactionBroker`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
[5{_recursiveTransaction="transaction"@"NSObject<OS_os_transaction>""opens"I}] _openTransactions;
```

## Class methods

```
+[BWDeferredTransactionBroker sharedInstance];
```

## Instance methods

```
-[BWDeferredTransactionBroker exitImmediately];
-[BWDeferredTransactionBroker closeTransaction:];
-[BWDeferredTransactionBroker openTransaction:];
-[BWDeferredTransactionBroker openTransaction:name:];
-[BWDeferredTransactionBroker openTransaction:pid:];
```
