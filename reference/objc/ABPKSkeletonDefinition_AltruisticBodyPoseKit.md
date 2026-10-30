# `ABPKSkeletonDefinition`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _jointNames;
{vector<long, std::allocator<long>>="__begin_"^q"__end_"^q""{?="__cap_"^q}} _jointParentIndicesVector;
{map<long, std::vector<long>, std::less<long>, std::allocator<std::pair<const long, std::vector<long>>>>="__tree_"{__tree<std::__value_type<long, std::vector<long>>, std::__map_value_compare<long, std::pair<const long, std::vector<long>>, std::less<long>>, std::allocator<std::pair<const long, std::vector<long>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _parentsToChildIndicesMap;
@"NSArray" _parentChildOrder;
@"NSDictionary" _jointNamesToIndices;
q _rootJointIndex;
```

## Properties

```
@property (TQ,R,N) jointCount;
@property (Tq,R,N,V_rootJointIndex) rootJointIndex;
@property (T@"NSArray",R,N,V_parentChildOrder) parentChildOrder;
```

## Class methods

```
+[ABPKSkeletonDefinition computeParentChildOrderFor:withRoot:];
```

## Instance methods

```
-[ABPKSkeletonDefinition init];
-[ABPKSkeletonDefinition initWithType:];
-[ABPKSkeletonDefinition jointCount];
-[ABPKSkeletonDefinition jointName:];
-[ABPKSkeletonDefinition parentJoint:];
-[ABPKSkeletonDefinition enumerateChildrenJointIndicesOfJointAtIndex:withBlock:];
-[ABPKSkeletonDefinition getChildrenIndices:];
-[ABPKSkeletonDefinition indexOfJointWithName:];
-[ABPKSkeletonDefinition initWithPlist:fromBundle:];
-[ABPKSkeletonDefinition parentChildOrder];
-[ABPKSkeletonDefinition rootJointIndex];
```
