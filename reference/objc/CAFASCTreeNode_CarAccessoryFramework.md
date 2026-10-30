# `CAFASCTreeNode`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 4 class methods

## Instance variables

```
@"NSString" _type;
@"NSString" _name;
@"NSDictionary" _children;
@"NSArray" _registeredValues;
```

## Properties

```
@property (T@"NSString",&,N,V_type) type;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSDictionary",&,N,V_children) children;
@property (T@"NSArray",&,N,V_registeredValues) registeredValues;
```

## Class methods

```
+[CAFASCTreeNode supportsSecureCoding];
+[CAFASCTreeNode nodeType:withName:];
+[CAFASCTreeNode nodeType:withString:];
+[CAFASCTreeNode nodeType:withType:];
```

## Instance methods

```
-[CAFASCTreeNode setChildren:];
-[CAFASCTreeNode setType:];
-[CAFASCTreeNode children];
-[CAFASCTreeNode type];
-[CAFASCTreeNode encodeWithCoder:];
-[CAFASCTreeNode description];
-[CAFASCTreeNode setName:];
-[CAFASCTreeNode initWithCoder:];
-[CAFASCTreeNode name];
-[CAFASCTreeNode _childNodeMatchingType:];
-[CAFASCTreeNode registeredValues];
-[CAFASCTreeNode setRegisteredValues:];
-[CAFASCTreeNode treeLogLinesIndent:];
```
