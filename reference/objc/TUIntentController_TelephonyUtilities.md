# `TUIntentController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 3 class methods

## Instance variables

```
@"<TUHandleContactProvider>" _contactProvider;
```

## Properties

```
@property (T@"<TUHandleContactProvider>",R,N,V_contactProvider) contactProvider;
```

## Class methods

```
+[TUIntentController tu_INPersonHandleForTUHandle:label:];
+[TUIntentController tu_INPersonHandleTypeForTUHandleType:];
+[TUIntentController tu_INPersonsFromHandle:contacts:];
```

## Instance methods

```
-[TUIntentController contactProvider];
-[TUIntentController initWithContactProvider:];
-[TUIntentController personsByHandleForHandles:];
-[TUIntentController startCallIntentByHandleForHandles:capability:destinationType:];
-[TUIntentController voicemailStartCallIntentByHandleForHandles:];
```
