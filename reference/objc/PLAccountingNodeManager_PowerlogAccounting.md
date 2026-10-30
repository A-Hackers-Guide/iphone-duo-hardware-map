# `PLAccountingNodeManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _nodeMappingLock;
@"NSMutableDictionary" _nodeNameToNodeID;
@"NSMutableDictionary" _nodeIDToNodeName;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_nodeNameToNodeID) nodeNameToNodeID;
@property (T@"NSMutableDictionary",&,V_nodeIDToNodeName) nodeIDToNodeName;
```

## Class methods

```
+[PLAccountingNodeManager sharedInstance];
```

## Instance methods

```
-[PLAccountingNodeManager init];
-[PLAccountingNodeManager nodeIDToNodeName];
-[PLAccountingNodeManager nodeNameForNodeID:];
-[PLAccountingNodeManager setNodeIDToNodeName:];
-[PLAccountingNodeManager childNodeIDsFromChildNodeNames:];
-[PLAccountingNodeManager nodeIDForNodeName:isPermanent:];
-[PLAccountingNodeManager nodeNameToNodeID];
-[PLAccountingNodeManager removeNodeReferenceFromCache:];
-[PLAccountingNodeManager setNodeNameToNodeID:];
-[PLAccountingNodeManager setupNodes];
```
