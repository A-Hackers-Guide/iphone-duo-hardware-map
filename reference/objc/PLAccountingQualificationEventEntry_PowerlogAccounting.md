# `PLAccountingQualificationEventEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingEventEntry`
- 1 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSSet" _childNodeIDs;
```

## Properties

```
@property (T@"NSNumber",R,N) qualificationID;
@property (T@"NSSet",R,N,V_childNodeIDs) childNodeIDs;
@property (T@"NSSet",R,N) childNodeNames;
```

## Class methods

```
+[PLAccountingQualificationEventEntry load];
```

## Instance methods

```
-[PLAccountingQualificationEventEntry qualificationID];
-[PLAccountingQualificationEventEntry subEntryKey];
-[PLAccountingQualificationEventEntry childNodeIDs];
-[PLAccountingQualificationEventEntry childNodeNames];
-[PLAccountingQualificationEventEntry initWithQualificationID:withChildNodeIDs:withRange:];
-[PLAccountingQualificationEventEntry initWithQualificationID:withChildNodeNames:withRange:];
-[PLAccountingQualificationEventEntry instanceDirectionality];
-[PLAccountingQualificationEventEntry isEmptyEvent];
-[PLAccountingQualificationEventEntry isEqualContentsWithEvent:];
```
