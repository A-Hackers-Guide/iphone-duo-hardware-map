# `/System/Library/PrivateFrameworks/MilAneflow.framework/MilAneflow`

iOS 27.2 dyld shared cache image. Version `1.104.0.0.0`. **[DSC]**

## Linked libraries (3)

- `/System/Library/PrivateFrameworks/MIL.framework/MIL`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`

## Strings (483)

```
'sparse_num_nonzero_per_filter' is incompatible with 'dense_kernel'
', violations: 
Cannot get value type for 
InputT
, got 
 of \"
rsqrt
_
x_sat_right should not be NaN
parameter '
Values of '
log2
 exceed limits, must in range [0, K] where K is the kernel_size at that dimension
\" operation requires broadcastable shape for \"
 op. Got 
\".
ne_maximum
y_scale
 on depth.
\", \"
Maximum kernel depth exceeded.
' is not supported for 
Input and output dtypes must match for reshape.
Initialized bias out of bounds of hardware constraints.
Not implemented. Shape inference for conv transpose.
index out of bounds
'pad' vector must have equal length to double the number of spatial dimensions.
Execution did not produce output value for 
pe_add
' does not handle immediate values
' has unsupported dtype.
slope_left
alpha
pe_less
 on height.
\" operation requires identical data types for \"
No value.
Illegal bias shift exponent.
Non constant bias vectors not yet implemented.
Scale must be 1, otherwise convert scale into post_scale and alpha. This restriction is an arbitrary behavior of pyANE compiler
Found unsupported dtype for output binding.
'palette_table' is incompatible with 'dense_kernel'
Interleave dim must be less thank (rank - 1) if interleave_amount is > 1.Unknown location
' has non tensor type.
 does not match inferred shape 
Conv padding support constraints violated for Px.
source.size() == target.size()
 into tensor of rank 
inputs must have static shape.
input_shape.size() == perm_positive.size()
Conv padding support constraints violated for Py.
TWICE_NUM_SPATIAL_DIMS
NUM_SPATIAL_DIMS_PLUS_ONE
XYBroadcastReducedShape
Activation inputs and outputs must have same data type.
\" and \"
Opset name is not an AneFlow opset: 
Strides on an individual conv must be positive 1 or 2. For larger strides, a decomposition must be used.
not implemented for weight rewrite
If lut_mode is INV, LOG2, SQR, SQRT, RSQRT, then x_sat_left should be non-negative
\", and output.
Size of '
Expected a channel vector for parameter shape.
Conv padding must be supported by kernel in width dimension.
'pad' parameter must have static shape.
conv
'
ne_mul
x_scale
Activation input and output must have same rank.
num_groups in groupwise conv must divide kernel dimension.
' in depth dimension, got: 
PePoolCpu.cpp
min
lut
Illegal weight dimension to split at index: 
)
Invalid stride for dimension 
scale
intercept_left should not be NaN, +inf or -inf.
frac
' does not resolve.
' already bound.
Channel vector shape must be static.
acc_left_shift
pe_reduce
pe_equal
YShape
ComputeValueAvgPool
Unsupported dtype.
FuseConvScale
Unimplemented output dtype
Alternative kernel (to dense) representations not yet implemented in MIL<aneflow>.
mul
\"
ShapeValidators.cpp
 bytes.
No value for y
src_shape.size() == mul_shape.size()
BatchX
Cannot specify both of 'dense_kernel' and 'alternative_format_kernel_coefficients'
kernel_sizes.size() == num_spatial_dims + 1
aneflowh2022
Expect same data type for input and output.
reduction_epsilon
Unhandled dtype for conv bias.
Input dimension depth exceed limits, expect [
kernel shape must be static.
kernel_sizes
group_kernel_reuse
pe_mul
PeReduceCpu.cpp
Value store has mismatched type for 
Unimplemented y dtype
ne_avg_pool
cos
promote_shape_to_5d
positive_perm[i] >= 0 && positive_perm[i] < rank
 for parameter \"
Expect kernel_sizes of height in range [1, 
' in depth dimension, got 
output
NePoolCpu.cpp
intercept_left
intercept_right should not be NaN, +inf or -inf.
Cannot get type as tensor for 
Invalid kernel dtype
 in range [1, 2], got 
reduction_scale
: 
dense_kernel
num_groups
replicate
transpose
Expect [ne_conv, pe/ne_mul] in pass 
'x' cannot be scalar
; 
aneflowh2021
Input dimension width exceed limits, expect [
' needs to be run before '
], got 
vector
XReducedShape
ne_batch_matmul
TransposeCpu.cpp
Dtype 
include_pads
reduce_mean: input tensor rank must >= 3.
base_ne_matmul
No value for x
reduction_post_processing
int
ne_activation with different input and output dtypes (with casting) is not implemented in the interpreted mode.
Kernel must have input channels equivalent to x's input channels over num_groups
reshape
Not implemented rank for weight translation: 
y_sat_right
transposed
pe_add_mul
sum
Shape is not statically known at dimension 
Value is not a tensor.
Kernel must have group dimension equal to 'num_groups' or 1 if 'group_kernel_reuse' is set.
'dilations' vector must have equal length to the number of spatial dimensions.
x_rank == o_shape.size()
 or 
Failed to parse conv parameters.
Invalid interleave dimension. Interleave > 1 requires dimension to be specified in the range [0, rank - 1).
maximum
Computed binary point plus post-right shift bounded by accumulator dest size. See op definition.
__ival_for_
PE pool value of 
's pattern
'dilations' parameter must have static shape.
Pad type not known: 
'.
ne_activation
Value is not a tensor for 
' to be array of size 
Must specify one of 'dense_kernel' and 'alternative_format_kernel_coefficients'
ceil_mode
GetIndex
DTypes not compatible with live tensors are not implemented in ANEFlow const. Violation at 
. Must be at least 
pad_mode
No value for dense_kernel
sparse_num_nonzero
relu
pe_min_pool
Illegal rank for conv weight translation: 
, 
Conv padding support constraints violated for Pz.
acc_bias_shift
pe_greater_equal
 for op '
o_shape.size() >= 3 && o_shape.size() <= 5
Pass '
Function output '
Unimplemented x dtype
matrix_vector_bias
Expect [ne_conv, ne_activation] in pass 
Zero detected for 'x' at dimension 
 in shapes 
Cin
Only tensors are handled for const attribute 
Attribute val is undefined for const op
' 
), got 
\" operation requires identical shapes for \"
 in operation \"
outputs must have static shape.
' has non-static shape.
Function does not have requested opset
ne_matmul
Activation input and output must have same shape.
 vs. 
Maximum kernel height exceeded.
kernel_sizes.back() == strides.back()
ios opset does not yet have quantized conv.
Output type is not a tensor.
Input rank must be >= 3
_fused
Rank must be in [1, 5] for strided options.
Conv padding must be supported by kernel in height dimension.
linear
Unsupported config for op '
Unexpected dtype copying to fp16.
GetRank5TensorIndex
 in shape 
sqr
Vector size wrong for 
ComputeValue
Output shape 
x_shape.size() >= 3 && x_shape.size() <= 5
 must be in range [-
PeElementWiseCpu.cpp
num_groups must be greater than 0.
pe_max_pool
Invalid 
ComputeValueMinMaxPool
alternative_format_kernel_coefficients
a
y_scale == 1.0 || y_scale == -1.0
Output rank 
Inferred zero or negative output size 
 does not match rank of input tensor of shape 
PE reduce: for N/D/H/C dims, reduce up to 2 dims is allowed.
src_shape.size() == add_shape.size()
post_scale
dilations
tanh
' violates size constraints
Const expected to have exactly one bound attribute named 
reduction
Conv input not a tensor
PyANE does not reuse bias or post-scale in group data, so channel vector configurations are not supported at the moment.
ne_max_pool
 on width.
\" and output.
Expected 
num_groups must divide input_channel.
exclude_padding_from_average
pe_greater
BatchXBatchYBroadcasted
ne_reduce is not implemented.
' not implemented
.
Channel does not match number of output filters.
x must have static shape.
reduction_axes
XShape
KCout
Expect kernel_sizes of width in range [1, 
\" must be less than 
custom
KMEM limits exceeded by kernel data.
' op. Got 
YDType
Cannot resolve output name 
Unknown location
Accumulator initialization out of range.
palette_table
NUM_FILTERS
NCDHW
Unexpected value for pad_mode.
XDType
strides.size() == num_spatial_dims + 1
Biases not matching the input type (fp16) are not implemented or expected from the iOS opset.
' got 
add
avg_pool
ne_piecewise_v2
Padding validation for conv transpose not implemented.
Conv padding must be supported by kernel in depth dimension.
Only mean reduction is supported at the moment.
PE reduce: duplicated axes not allowed.
Stride programming constraint 6.1.6.1.1 violated.
intercept_right
pre_relu
y
PE reduce: for W dim, if its input dim size is not 1, it should be reduced (W should appear in reduction_axis).
keep_dims
Unexpected rank 
pe_abs
 does not match rank of inferred shape 
Dilation must be greater than zero.
Fp32 precision (for bias) not supported by ANE.
NUM_GROUPS
perm
'  must have static shape.
sign_mode
NDHWC
Interleave amount must be non-zero. 1 is effectively no interleave
post_processing not implemented.
NUM_REDUCTION_AXES
y_shape.size() >= 3 && y_shape.size() <= 5
\" in operation \"
NE: 
Value store does not have function input 
lrelu
split_lut
reduce_mean: keep_dim must be true.
shape.size() == positive_perm.size()
Alpha is out of range (0 < alpha < 1).
Unsupported scale data type, must be one of [fp16, int8, uint8]
pe_add_abs
max
No value for 
Dynamic weight translation not implemented for conv.
custom_pads
Unimplemented type for 
PALETTE_SIZE
y_sat_right should not be NaN
Input dimension height exceed limits, expect [
x_sat_right
Negative strides are not implemented.
 does not match rank of x 
'sparse_mask' is incompatible with 'dense_kernel'
reduce_mean
slope_right should not be NaN, +inf or -inf.
Bias shift exponent outside of hardware capabilities. Computed shift must 32 bit and be <= 11.
KernelT
SPARSE_MASK_SIZE
PE does not support '
'x' and output must have equal number of elements.
Strides do not match rank for '
sparse_num_nonzero_per_filter
NWC
Unimplemented 'reduction': rdar://86732114
shape5d.size() == 5
y_sat_left
pe_square
Attribute val must be tensor with static shape
Output must be tensor with static shape
pe_minimum
pe_not_equal
sqrt
Immediate value inputs not handled.
Conv does not handle immediate value inputs for x
Expect same channel dimension for '
Aneflow dialect's const output does not support type attributes.
map::at:  key not found
ne_conv
'strides' parameter must have static shape.
slope_right
x_sat_left should not be NaN
InferTransposeOutputShape
pe_avg_pool
x_sat_left
Batch
pe_add_square
Unsupported input rank 
. Violated at 
strides
const
Cannot resolve function name 
x
bias
pad
ComputeValuePeReduce
' and '
Sum of input channel sizes for \"
Zero detected for 'y' at dimension 
ALTERNATE_KERNEL_SIZE
slope_left should not be NaN, +inf or -inf.
Conv input, weights, and output must be supported dtype.
Matrix inner dimension mismatch, tensor y must have inner dimension 
Unsupported dtype for reshape.
Found inconsistent type for parameter \"
weight
x_rank == perm.size()
NeBatchMatmulCpu.cpp
shape.size() >= 0 && shape.size() <= 5
OpTranslator.cpp
pe_maximum
x_sat_left should be smaller than x_sat_right
Maximum kernel width exceeded.
kernel
pe_less_equal
XYBroadcastShape
Did not find value for output 
kernel dimension must have spatial dims equal to number of spatial dimensions of input.
Expected '
Op not in table of functions: 
Cannot resolve opset name 
Output should have the same rank as x parameter
Bias tensor must be of shape (
If lut_mode is FRAC or INT then in_abs must be True.
MIL<aneflow> frontend has not yet implemented dilated conv.
post_right_shift
 in range [1, 5], got 
same
missing translate function for op 
Weight rewrite not implemented for 
y_sat_left should not be NaN
reduction_post_processing is not supported at the moment.
Translation for '
PE: 
in_abs
ne_square
Expect '
Expect kernel_sizes of depth in range [1, 
sz == 1
Produced target that fails validation with: 
negzero
max_pool
Execution error running op: 
invert
ne_minimum
NCW
Cannot resolve input name 
valid
strides.size() == num_spatial_dims
'x' must be tensor with static shape
Incompatible at dimension 
Conv input, weights, and output must be tensors.
Dimension extent invalid for parameter 
Function input '
basic_string
Input '
aneflowh2020
 at index 
Const not expected to have bound parameters. Violated at 
sin
Function not implemented.
Output cannot be scalar
inv
Post scale tensor must be of shape (
Attribute val has incompatible type with operation output
weights must have static shape.
\" operation requires identical shape for \"
'sparse_num_nonzero' is incompatible with 'dense_kernel'
Padding validation for dilated convs not yet implemented.
Unimplemented input dtype
InferTransposedShape
Activation input and output must have known shape.
Unimplemented pad: rdar://84906152
y_intercept
kernel_sizes.size() == num_spatial_dims
' is not a tensor.
val
GetShapePermInfoFromAxisConvention
,)
sparse_mask
NUM_SPATIAL_DIMS
OutputT
ne_reduce
Can't retrieve weight value for 
No neural engine activation function for op 
Invalid operator: '
AlternateKernelT
get_index
ne_add
ne_min_pool
Expect 
kd == 1
Not implemented.
' must have length of 
BatchY
Found unsupported dtype for binding.
sigmoid
'strides' vector must have equal length to the number of spatial dimensions.
lut_mode
```
