# `WCAFetchSQLiteRequest`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WCAFetchRequest`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _parameters;
@"NSString" _tableName;
@"NSArray" _columnNames;
q _limit;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_parameters) parameters;
@property (T@"NSString",C,N,V_tableName) tableName;
@property (T@"NSArray",C,N,V_columnNames) columnNames;
@property (Tq,N,V_limit) limit;
```

## Class methods

```
+[WCAFetchSQLiteRequest supportsSecureCoding];
```

## Instance methods

```
-[WCAFetchSQLiteRequest parameters];
-[WCAFetchSQLiteRequest setTableName:];
-[WCAFetchSQLiteRequest setParameters:];
-[WCAFetchSQLiteRequest limit];
-[WCAFetchSQLiteRequest columnNames];
-[WCAFetchSQLiteRequest tableName];
-[WCAFetchSQLiteRequest encodeWithCoder:];
-[WCAFetchSQLiteRequest description];
-[WCAFetchSQLiteRequest initWithCoder:];
-[WCAFetchSQLiteRequest setLimit:];
-[WCAFetchSQLiteRequest setColumnNames:];
```
