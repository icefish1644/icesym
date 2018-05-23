typedef struct
{
  double time, dt, dtheta_rpm, Courant, ga, R_gas, theta, omega, rpm, 
    rpm_ini, theta_cycle, ga_intake, ga_exhaust, tol;
  int iter_sim1d, viscous_flow, heat_flow, icycle, engine_type,
    ncyl, has_converged, nzones;
  bool save_extras, use_global_gas_prop, debug;
} dataSim;

typedef struct
{
  double Bore, crank_radius, Vol_clearance, rod_length, head_chamber_area,
    piston_area, theta_0, delta_ca, Twall, factor_ht, major_radius,
    minor_radius, chamber_heigh, converge_var_old, converge_var_new;
  int nnod_input, nvi, nve, nnod, ndof, model_ht, type_ig, nunit, 
    species_model, ntemp, nvanes, converge_mode;
  bool scavenge, full_implicit,nh_temp;
} dataCylinder;


typedef struct
{
  double longitud, dt_max, Text, esp, K;
  int nnod, ndof, nnod_input, t_left, t_right, type;;
} dataTube;

typedef struct
{
  double Volume, mass, h_film, Area_wall, T_wall;
  int nnod, ndof, nnod_input, nunit, type;
} dataTank;

typedef struct
{   
  //vector<int> type_end;
  int nnod, ndof, nnod_input, modelo_junc, type;
  //vector<double> state, new_state, Area;
} dataJunction;
