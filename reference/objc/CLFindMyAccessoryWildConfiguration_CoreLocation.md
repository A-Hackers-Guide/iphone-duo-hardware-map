# `CLFindMyAccessoryWildConfiguration`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
S _keysRemaining;
S _keyCount;
I _keyRollInterval;
@"NSDate" _desiredKeyRollDate;
```

## Properties

```
@property (T@"NSDate",R,V_desiredKeyRollDate) desiredKeyRollDate;
@property (TI,R,V_keyRollInterval) keyRollInterval;
@property (TS,R,V_keysRemaining) keysRemaining;
@property (TS,R,V_keyCount) keyCount;
```

## Class methods

```
+[CLFindMyAccessoryWildConfiguration supportsSecureCoding];
```

## Instance methods

```
-[CLFindMyAccessoryWildConfiguration init];
-[CLFindMyAccessoryWildConfiguration dealloc];
-[CLFindMyAccessoryWildConfiguration encodeWithCoder:];
-[CLFindMyAccessoryWildConfiguration description];
-[CLFindMyAccessoryWildConfiguration initWithCoder:];
-[CLFindMyAccessoryWildConfiguration keyRollInterval];
-[CLFindMyAccessoryWildConfiguration desiredKeyRollDate];
-[CLFindMyAccessoryWildConfiguration encodeConfiguration];
-[CLFindMyAccessoryWildConfiguration initWithDesiredNextKeyRollDate:keyRollInterval:keysRemainingInWildPeriod:wildPeriodKeyCount:];
-[CLFindMyAccessoryWildConfiguration keyCount];
-[CLFindMyAccessoryWildConfiguration keysRemaining];
```
