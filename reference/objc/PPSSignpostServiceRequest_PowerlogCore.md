# `PPSSignpostServiceRequest`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
i _type;
@"NSDate" _endDate;
@"NSURL" _sourceURL;
@"NSDate" _startDate;
@"NSUUID" _uuid;
```

## Properties

```
@property (T@"NSDate",&,V_endDate) endDate;
@property (T@"NSURL",&,V_sourceURL) sourceURL;
@property (T@"NSDate",&,V_startDate) startDate;
@property (Ti,V_type) type;
@property (T@"NSUUID",R,V_uuid) uuid;
```

## Class methods

```
+[PPSSignpostServiceRequest supportsSecureCoding];
```

## Instance methods

```
-[PPSSignpostServiceRequest sourceURL];
-[PPSSignpostServiceRequest startDate];
-[PPSSignpostServiceRequest setSourceURL:];
-[PPSSignpostServiceRequest setStartDate:];
-[PPSSignpostServiceRequest uuid];
-[PPSSignpostServiceRequest init];
-[PPSSignpostServiceRequest endDate];
-[PPSSignpostServiceRequest setType:];
-[PPSSignpostServiceRequest setEndDate:];
-[PPSSignpostServiceRequest type];
-[PPSSignpostServiceRequest encodeWithCoder:];
-[PPSSignpostServiceRequest description];
-[PPSSignpostServiceRequest initWithCoder:];
```
