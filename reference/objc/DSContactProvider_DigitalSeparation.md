# `DSContactProvider`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _contactStoreWorkQueue;
@"CNContactStore" _store;
```

## Properties

```
@property (T@"CNContactStore",&,N,V_store) store;
```

## Class methods

```
+[DSContactProvider defaultProvider];
```

## Instance methods

```
-[DSContactProvider initWithStore:];
-[DSContactProvider keysToFetch];
-[DSContactProvider store];
-[DSContactProvider init];
-[DSContactProvider setStore:];
-[DSContactProvider sanitizeContacts:];
-[DSContactProvider unifiedContactInDictionary:forIdentity:];
-[DSContactProvider unifiedContactsDictionaryForHandleStrings:];
-[DSContactProvider unifiedContactsDictionaryForIdentities:];
-[DSContactProvider unifiedContactsForContactIdentifiers:];
```
