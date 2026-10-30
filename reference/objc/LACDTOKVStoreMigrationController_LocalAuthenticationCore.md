# `LACDTOKVStoreMigrationController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOKVStoreMigrationController`
- 3 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOKVStore>" _store;
@"<LACGlobalDomainDTO>" _defaults;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOKVStoreMigrationController performMigrationIfNeeded];
-[LACDTOKVStoreMigrationController _migrateStrictModeKeyIfNeededWithCompletion:];
-[LACDTOKVStoreMigrationController initWithKVStore:defaults:workQueue:];
```
