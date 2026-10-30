# `BioUserDefaults`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 17 instance methods, 5 class methods

## Instance variables

```
@"NSMutableDictionary" _registeredDefaults;
@"NSMutableArray" _updateBlocks;
```

## Class methods

```
+[BioUserDefaults sharedInstance];
+[BioUserDefaults initialize];
+[BioUserDefaults removeAllPreferences];
+[BioUserDefaults preferenceObjectForKey:];
+[BioUserDefaults removeLegacyPreferences];
```

## Instance methods

```
-[BioUserDefaults stringForKey:];
-[BioUserDefaults integerForKey:];
-[BioUserDefaults boolForKey:];
-[BioUserDefaults synchronize];
-[BioUserDefaults intForKey:];
-[BioUserDefaults objectOfClass:forKey:];
-[BioUserDefaults unsignedIntForKey:];
-[BioUserDefaults unsignedIntegerForKey:];
-[BioUserDefaults objectForKey:];
-[BioUserDefaults unregisterUpdateNotification:];
-[BioUserDefaults registerDefaults:];
-[BioUserDefaults stateDictionary];
-[BioUserDefaults setObject:forKey:];
-[BioUserDefaults setBool:forKey:];
-[BioUserDefaults numberForKey:];
-[BioUserDefaults updateNotification];
-[BioUserDefaults registerUpdateNotification:];
```
