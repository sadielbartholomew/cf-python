from .abstract import CylindricalGridMapping
from .abstract.gridmappingbase import _validate_map_parameter


class Mercator(CylindricalGridMapping):
    """The Mercator grid mapping.

    See the CF Conventions document 'Appendix F: Grid Mappings' sub-section on
    this grid mapping:

    http://cfconventions.org/Data/cf-conventions/cf-conventions-1.10/
    cf-conventions.html#_mercator

    or the corresponding PROJ projection page:

    https://proj.org/en/9.2/operations/projections/merc.html

    for more information.

    .. versionadded:: GMVER

    :Parameters:

        false_easting: number or scalar `Data`, optional
            The false easting (PROJ 'x_0') value.
            If provided as a number or `Data` without units, the units
            are taken as metres 'm', else the `Data` units are
            taken and must be compatible with distance.
            The default is 0.0 metres.

        false_northing: number or scalar `Data`, optional
            The false northing (PROJ 'y_0') value.
            If provided as a number or `Data` without units, the units
            are taken as metres 'm', else the `Data` units are
            taken and must be compatible with distance.
            The default is 0.0 metres.

        standard_parallel: 2-`tuple` of number or scalar `Data`
                           or `None`, optional
            The standard parallel value(s): the first (PROJ 'lat_1'
            value) and/or the second (PROJ 'lat_2' value), given
            as a 2-tuple of numbers or strings corresponding to
            the first and then the second in order, where `None`
            indicates that a value is not being set for either.

            If provided as a number or `Data` without units, the units
            for each of the values are taken as 'degrees_north', else
            the `Data` units are taken and must be angular and
            compatible with latitude.

            The default is (0.0, 0.0), that is 0.0 degrees_north
            for the first and second standard parallel values.

        longitude_of_projection_origin: number or scalar `Data`, optional
            The longitude of projection center (PROJ 'lon_0' value).
            If provided as a number or `Data` without units, the units
            are taken as 'degrees_east', else the `Data` units are
            taken and must be angular and compatible with longitude.
            The default is 0.0 degrees_east.

        scale_factor_at_projection_origin: number or scalar `Data`, optional
            The scale factor used in the projection (PROJ 'k_0' value).
            Unitless, so `Data` must be unitless. The default is 1.0.

    """

    grid_mapping_name = "mercator"
    proj_id = "merc"

    def __init__(
        self,
        false_easting=0.0,
        false_northing=0.0,
        standard_parallel=(0.0, 0.0),
        longitude_of_projection_origin=0.0,
        scale_factor_at_projection_origin=1.0,
        **kwargs,
    ):
        super().__init__(
            false_easting=false_easting,
            false_northing=false_northing,
            **kwargs,
        )

        self.standard_parallel = (
            _validate_map_parameter("standard_parallel", standard_parallel[0]),
            _validate_map_parameter("standard_parallel", standard_parallel[1]),
        )
        self.longitude_of_projection_origin = _validate_map_parameter(
            "longitude_of_projection_origin", longitude_of_projection_origin
        )
        self.scale_factor_at_projection_origin = _validate_map_parameter(
            "scale_factor_at_projection_origin",
            scale_factor_at_projection_origin,
        )