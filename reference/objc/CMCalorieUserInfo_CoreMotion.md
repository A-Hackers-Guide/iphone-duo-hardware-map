# `CMCalorieUserInfo`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 6 instance variables, 6 properties, 14 instance methods, 2 class methods

## Instance variables

```
d fAge;
q fGender;
d fHeight;
d fWeight;
q fCondition;
B fBetaBlockerUse;
```

## Properties

```
@property (Tq,R,N) gender;
@property (Td,R,N) age;
@property (Td,R,N) height;
@property (Td,R,N) weight;
@property (Tq,R,N) condition;
@property (TB,R,N) betaBlockerUse;
```

## Class methods

```
+[CMCalorieUserInfo supportsSecureCoding];
+[CMCalorieUserInfo genderString:];
```

## Instance methods

```
-[CMCalorieUserInfo condition];
-[CMCalorieUserInfo age];
-[CMCalorieUserInfo dealloc];
-[CMCalorieUserInfo weight];
-[CMCalorieUserInfo encodeWithCoder:];
-[CMCalorieUserInfo description];
-[CMCalorieUserInfo initWithCoder:];
-[CMCalorieUserInfo copyWithZone:];
-[CMCalorieUserInfo height];
-[CMCalorieUserInfo gender];
-[CMCalorieUserInfo initWithAge:gender:height:weight:condition:];
-[CMCalorieUserInfo betaBlockerUse];
-[CMCalorieUserInfo initWithAge:gender:height:weight:];
-[CMCalorieUserInfo initWithAge:gender:height:weight:condition:betaBlockerUse:];
```
