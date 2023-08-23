import argparse
from src.solver import PICsolver

def parsing():
    parser = argparse.ArgumentParser(description="PIC code for plasma simulation: 1D ")
    parser.add_argument("--num_particle", type = int, default = 50000)
    parser.add_argument("--num_mesh", type = int, default = 500)
    parser.add_argument("--t_min", type = float, default = 0)
    parser.add_argument("--t_max", type = float, default = 100)
    parser.add_argument("--dt", type = float, default = 1)
    parser.add_argument("--L", type = float, default = 50)
    parser.add_argument("--n0", type = float, default = 1.0)
    parser.add_argument("--vb", type = float, default = 3.0)
    parser.add_argument("--vth", type = float, default = 1.0)
    parser.add_argument("--gamma", type = float, default = 5.0)
    parser.add_argument("--use_animation", type = bool, default = True)
    parser.add_argument("--plot_freq", type = int, default = 10)
    parser.add_argument("--save_dir", type = str, default = "./result/simulation.gif")
    args = vars(parser.parse_args())
    return args

if __name__ == "__main__":
    
    args = parsing()
    solver = PICsolver(
        N = args['num_particle'],
        N_mesh=args['num_mesh'],
        n0 = args['n0'],
        L = args['L'],
        dt = args['dt'],
        tmin = args['t_min'],
        tmax = args['t_max'],
        gamma = args['gamma'],
        vth = args['vth'],
        vb = args['vb'],
        use_animation=args['use_animation'],
        plot_freq=args['plot_freq'],  
        save_dir = args['save_dir']
    )
    
    solver.solve()