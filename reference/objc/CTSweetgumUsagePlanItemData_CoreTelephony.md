# `CTSweetgumUsagePlanItemData`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
q _units;
@"NSString" _capacity;
@"NSString" _maxDataBeforeThrottling;
@"NSString" _thisDeviceDataUsed;
@"NSString" _sharedDataUsed;
@"NSString" _sharedPlanIdentifier;
```

## Properties

```
@property (Tq,N,V_units) units;
@property (T@"NSString",&,N,V_capacity) capacity;
@property (T@"NSString",&,N,V_maxDataBeforeThrottling) maxDataBeforeThrottling;
@property (T@"NSString",&,N,V_thisDeviceDataUsed) thisDeviceDataUsed;
@property (T@"NSString",&,N,V_sharedDataUsed) sharedDataUsed;
@property (T@"NSString",&,N,V_sharedPlanIdentifier) sharedPlanIdentifier;
```

## Class methods

```
+[CTSweetgumUsagePlanItemData supportsSecureCoding];
```

## Instance methods

```
-[CTSweetgumUsagePlanItemData setCapacity:];
-[CTSweetgumUsagePlanItemData units];
-[CTSweetgumUsagePlanItemData setUnits:];
-[CTSweetgumUsagePlanItemData capacity];
-[CTSweetgumUsagePlanItemData init];
-[CTSweetgumUsagePlanItemData encodeWithCoder:];
-[CTSweetgumUsagePlanItemData description];
-[CTSweetgumUsagePlanItemData initWithCoder:];
-[CTSweetgumUsagePlanItemData isEqual:];
-[CTSweetgumUsagePlanItemData maxDataBeforeThrottling];
-[CTSweetgumUsagePlanItemData setMaxDataBeforeThrottling:];
-[CTSweetgumUsagePlanItemData setSharedDataUsed:];
-[CTSweetgumUsagePlanItemData setSharedPlanIdentifier:];
-[CTSweetgumUsagePlanItemData setThisDeviceDataUsed:];
-[CTSweetgumUsagePlanItemData sharedDataUsed];
-[CTSweetgumUsagePlanItemData sharedPlanIdentifier];
-[CTSweetgumUsagePlanItemData thisDeviceDataUsed];
```
