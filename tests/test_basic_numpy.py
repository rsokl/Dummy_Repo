import hypothesis.extra.numpy as hnp
import hypothesis.strategies as st
import numpy as np
from hypothesis import given
from numpy.testing import assert_allclose

from rsokl_dummy.numpy_functions import pairwise_dists

import pytest


@pytest.mark.parametrize(
    ("x, y, expected_dists"),
    [
        (
            np.array([[1.0, 0.0], [1.0, 1.0]]),
            np.array([[1.0, 0.0], [0.0, 1.0]]),
            np.array([[0.0, 2 / np.sqrt(2)], [1.0, 1.0]]),
        )
    ],
)
def test_pairwise_distances_known_inputs(x, y, expected_dists):
    assert_allclose(actual=pairwise_dists(x, y), desired=expected_dists)


#################################################################
# Implementing various property-based tests for `pairwise_dists`#
#################################################################


@given(
    shapes=hnp.mutually_broadcastable_shapes(
        signature="(n,d),(m,d)->(n,m)", max_dims=0
    ),
    data=st.data(),
)
def test_pairwise_dists_is_positive(
    shapes: hnp.BroadcastableShapes, data: st.DataObject
):
    shape_a, shape_b = shapes.input_shapes

    array_a = data.draw(
        hnp.arrays(shape=shape_a, dtype=np.float64, elements=st.floats(-1e9, 1e9)),
        label="array_a",
    )

    array_b = data.draw(
        hnp.arrays(shape=shape_b, dtype=np.float64, elements=st.floats(-1e9, 1e9)),
        label="array_b",
    )

    dists = pairwise_dists(array_a, array_b)

    assert np.all(dists >= 0)


@given(
    shapes=hnp.mutually_broadcastable_shapes(
        signature="(n,d),(m,d)->(n,m)", max_dims=0
    ),
    data=st.data(),
)
def test_pairwise_dists_is_symmetric(
    shapes: hnp.BroadcastableShapes, data: st.DataObject
):
    shape_a, shape_b = shapes.input_shapes

    array_a = data.draw(
        hnp.arrays(shape=shape_a, dtype=np.float64, elements=st.floats(-1e3, 1e3)),
        label="array_a",
    )

    array_b = data.draw(
        hnp.arrays(shape=shape_b, dtype=np.float64, elements=st.floats(-1e3, 1e3)),
        label="array_b",
    )

    dists = pairwise_dists(array_a, array_b)
    dists_transpose = pairwise_dists(array_b, array_a)

    assert_allclose(dists.T, dists_transpose, atol=1e-4, rtol=1e-4)


@given(
    shapes=hnp.mutually_broadcastable_shapes(
        signature="(n,d),(m,d)->(n,m)", max_dims=0
    ),
    data=st.data(),
)
def test_pairwise_dists_is_translation_invariant(
    shapes: hnp.BroadcastableShapes, data: st.DataObject
):
    shape_a, shape_b = shapes.input_shapes

    offset = data.draw(
        hnp.arrays(
            shape=(shape_a[1],), dtype=np.float64, elements=st.floats(-1e2, 1e2)
        ),
        label="offset",
    )
    array_a = data.draw(
        hnp.arrays(shape=shape_a, dtype=np.float64, elements=st.floats(-1e3, 1e3)),
        label="array_a",
    )

    array_b = data.draw(
        hnp.arrays(shape=shape_b, dtype=np.float64, elements=st.floats(-1e3, 1e3)),
        label="array_b",
    )

    dists = pairwise_dists(array_a, array_b)
    dists_w_offset = pairwise_dists(array_a + offset, array_b + offset)

    assert_allclose(dists, dists_w_offset, atol=1e-4, rtol=1e-4)
