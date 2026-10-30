# `CTXPCMigrateAppDataRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCRequestMessage`
- 0 instance variables, 2 properties, 6 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",R,N) sourceBundleID;
@property (T@"NSString",R,N) destinationBundleID;
```

## Class methods

```
+[CTXPCMigrateAppDataRequest allowedClassesForArguments];
+[CTXPCMigrateAppDataRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCMigrateAppDataRequest requiredEntitlement];
-[CTXPCMigrateAppDataRequest ct_shortName];
-[CTXPCMigrateAppDataRequest performRequestWithHandler:completionHandler:];
-[CTXPCMigrateAppDataRequest sourceBundleID];
-[CTXPCMigrateAppDataRequest destinationBundleID];
-[CTXPCMigrateAppDataRequest initWithSourceBundleID:destinationBundleID:];
```
