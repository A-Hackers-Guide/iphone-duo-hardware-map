# `CMTableCursor`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
Q _recordId;
Q _cachedLastRecordId;
Q _datatype;
@"NSString" _tableName;
```

## Properties

```
@property (TQ,N,V_recordId) recordId;
@property (TQ,N,V_cachedLastRecordId) cachedLastRecordId;
@property (TQ,R,N,V_datatype) datatype;
@property (T@"NSString",&,N,V_tableName) tableName;
```

## Class methods

```
+[CMTableCursor supportsSecureCoding];
```

## Instance methods

```
-[CMTableCursor setRecordId:];
-[CMTableCursor setTableName:];
-[CMTableCursor recordId];
-[CMTableCursor dealloc];
-[CMTableCursor datatype];
-[CMTableCursor tableName];
-[CMTableCursor encodeWithCoder:];
-[CMTableCursor hash];
-[CMTableCursor description];
-[CMTableCursor initWithCoder:];
-[CMTableCursor copyWithZone:];
-[CMTableCursor isEqual:];
-[CMTableCursor cachedLastRecordId];
-[CMTableCursor initWithDatatype:];
-[CMTableCursor setCachedLastRecordId:];
```
