# `MTLBVHDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 29 instance variables, 25 properties, 57 instance methods, 0 class methods

## Instance variables

```
Q _maxDepth;
Q _clampedMaxDepth;
Q _fragmentCount;
Q _primitiveDataSize;
@"MTLAccelerationStructureDescriptor" _mtlDescriptor;
{PipelineKey=""{?="pipelineIndex"b8"polygonType"b2"minFragmentsPerLeaf"b4"maxFragmentsPerLeaf"b8"indexStride"b4"spatialSplits"b1"useResourceBuffer"b1"primitiveMotion"b1"branchingFactor"b4"motion"b1"useBatching"b1"useChildIndices"b1"vertexFormat"b6"logThreadgroupSize"b4"maxFragmentsPerInnerNode"b8"createLeafNodes"b1"enforceMaxDepth"b1"useTemporalSplits"b1"disallowMixingTemporalSplitsAndLeafNodes"b1"useFastWideBuild"b1"deterministic"b1"fragmentPhase"b1"supportsSIMDReduction"b1"supportsSIMDShuffleAndFill"b1"useFastBestObjectSplit"b1"maxSubKeyframeTemporalSplits"b4"disallowTemporalSplits"b1"rowMajorInstanceMatrix"b1"refitUpdatesOpacityAndFunctionTableOffset"b1}"vertexStride"I"boundingBoxStride"I"minOverlap"f"traversalCost"f"fragmentCost"f"temporalSplitBias"f} _pipelineKey;
B _pipelineKeyValid;
B _motion;
B _useTemporalSplits;
B _disallowMixingTemporalSplitsAndLeafNodes;
B _useFastBuild;
B _deterministic;
f _primitiveCost;
f _traversalCost;
f _motionTraversalCost;
f _primitiveMotionStartTime;
f _primitiveMotionEndTime;
f _temporalSplitBias;
f _splitCapacity;
f _minOverlap;
Q _branchingFactor;
Q _minPrimitivesPerLeaf;
Q _maxPrimitivesPerLeaf;
Q _minPrimitivesPerInnerNode;
Q _maxPrimitivesPerInnerNode;
@"NSArray" _geometryDescriptors;
Q _primitiveKeyframeCount;
Q _maxSubKeyframeTemporalSplits;
Q _splitHeuristic;
```

## Properties

```
@property (TQ,N) maxDepth;
@property (TQ,N,V_branchingFactor) branchingFactor;
@property (TQ,N,V_minPrimitivesPerLeaf) minPrimitivesPerLeaf;
@property (TQ,N,V_maxPrimitivesPerLeaf) maxPrimitivesPerLeaf;
@property (TQ,N,V_minPrimitivesPerInnerNode) minPrimitivesPerInnerNode;
@property (TQ,N,V_maxPrimitivesPerInnerNode) maxPrimitivesPerInnerNode;
@property (Tf,N,V_traversalCost) traversalCost;
@property (Tf,N,V_primitiveCost) primitiveCost;
@property (TQ,N,V_splitHeuristic) splitHeuristic;
@property (Tf,N,V_splitCapacity) splitCapacity;
@property (Tf,N,V_minOverlap) minOverlap;
@property (Tf,N,V_motionTraversalCost) motionTraversalCost;
@property (TB,N,V_motion) motion;
@property (TQ,N,V_primitiveKeyframeCount) primitiveKeyframeCount;
@property (Tf,N,V_primitiveMotionStartTime) primitiveMotionStartTime;
@property (Tf,N,V_primitiveMotionEndTime) primitiveMotionEndTime;
@property (TB,N,V_useTemporalSplits) useTemporalSplits;
@property (Tf,N,V_temporalSplitBias) temporalSplitBias;
@property (TB,N,V_disallowMixingTemporalSplitsAndLeafNodes) disallowMixingTemporalSplitsAndLeafNodes;
@property (TB,N,V_useFastBuild) useFastBuild;
@property (TB,N,V_deterministic) deterministic;
@property (TQ,N,V_maxSubKeyframeTemporalSplits) maxSubKeyframeTemporalSplits;
@property (TQ,N) fragmentCount;
@property (TQ,N) primitiveDataSize;
@property (T@"NSArray",W,N,V_geometryDescriptors) geometryDescriptors;
```

## Instance methods

```
-[MTLBVHDescriptor init];
-[MTLBVHDescriptor fragmentCount];
-[MTLBVHDescriptor maxDepth];
-[MTLBVHDescriptor branchingFactor];
-[MTLBVHDescriptor primitiveMotion];
-[MTLBVHDescriptor actualMaxDepth];
-[MTLBVHDescriptor cachedPipelineKey];
-[MTLBVHDescriptor deterministic];
-[MTLBVHDescriptor disallowMixingTemporalSplitsAndLeafNodes];
-[MTLBVHDescriptor geometryDescriptors];
-[MTLBVHDescriptor maxPrimitivesPerInnerNode];
-[MTLBVHDescriptor maxPrimitivesPerLeaf];
-[MTLBVHDescriptor maxSubKeyframeTemporalSplits];
-[MTLBVHDescriptor minOverlap];
-[MTLBVHDescriptor minPrimitivesPerInnerNode];
-[MTLBVHDescriptor minPrimitivesPerLeaf];
-[MTLBVHDescriptor motion];
-[MTLBVHDescriptor motionTraversalCost];
-[MTLBVHDescriptor primitiveCost];
-[MTLBVHDescriptor primitiveDataSize];
-[MTLBVHDescriptor primitiveKeyframeCount];
-[MTLBVHDescriptor primitiveMotionEndTime];
-[MTLBVHDescriptor primitiveMotionStartTime];
-[MTLBVHDescriptor requiresResourceBuffer];
-[MTLBVHDescriptor setBranchingFactor:];
-[MTLBVHDescriptor setDeterministic:];
-[MTLBVHDescriptor setDisallowMixingTemporalSplitsAndLeafNodes:];
-[MTLBVHDescriptor setFragmentCount:];
-[MTLBVHDescriptor setGeometryDescriptors:];
-[MTLBVHDescriptor setMaxDepth:];
-[MTLBVHDescriptor setMaxPrimitivesPerInnerNode:];
-[MTLBVHDescriptor setMaxPrimitivesPerLeaf:];
-[MTLBVHDescriptor setMaxSubKeyframeTemporalSplits:];
-[MTLBVHDescriptor setMinOverlap:];
-[MTLBVHDescriptor setMinPrimitivesPerInnerNode:];
-[MTLBVHDescriptor setMinPrimitivesPerLeaf:];
-[MTLBVHDescriptor setMotion:];
-[MTLBVHDescriptor setMotionTraversalCost:];
-[MTLBVHDescriptor setPrimitiveCost:];
-[MTLBVHDescriptor setPrimitiveDataSize:];
-[MTLBVHDescriptor setPrimitiveKeyframeCount:];
-[MTLBVHDescriptor setPrimitiveMotionEndTime:];
-[MTLBVHDescriptor setPrimitiveMotionStartTime:];
-[MTLBVHDescriptor setSplitCapacity:];
-[MTLBVHDescriptor setSplitHeuristic:];
-[MTLBVHDescriptor setTemporalSplitBias:];
-[MTLBVHDescriptor setTraversalCost:];
-[MTLBVHDescriptor setUseFastBuild:];
-[MTLBVHDescriptor setUseTemporalSplits:];
-[MTLBVHDescriptor splitCapacity];
-[MTLBVHDescriptor splitHeuristic];
-[MTLBVHDescriptor temporalSplitBias];
-[MTLBVHDescriptor traversalCost];
-[MTLBVHDescriptor updateMaxDepth];
-[MTLBVHDescriptor updatePipelineKey];
-[MTLBVHDescriptor useFastBuild];
-[MTLBVHDescriptor useTemporalSplits];
```
